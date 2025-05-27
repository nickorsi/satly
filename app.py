import os
import requests

from dotenv import load_dotenv
from flask import Flask, redirect, flash, render_template, url_for, jsonify
from flask_debugtoolbar import DebugToolbarExtension
from sqlalchemy.sql.expression import func
from forms import AddPhotoForm, EditPhotoForm
from PIL import Image
from helpers import s3_upload
from datetime import datetime
from urllib.parse import quote_plus
from models import db, connect_db, Photo

load_dotenv()

AWS_ACCESS_KEY_ID = os.getenv('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = os.getenv('AWS_SECRET_ACCESS_KEY')
S3_BUCKET = os.getenv('S3_BUCKET')
BASE_URL = f'https://{S3_BUCKET}.s3.us-west-1.amazonaws.com'
PASSWORD = quote_plus(os.getenv('password'))
USER = os.getenv('user')
HOST = os.getenv('host')
PORT = os.getenv('port')
DBNAME = os.getenv('dbname')
DATA_BASE_URL = f"postgresql+psycopg2://{USER}:{PASSWORD}@{HOST}:{PORT}/{DBNAME}?sslmode=require"

app = Flask(__name__)
app.config['SECRET_KEY'] = AWS_SECRET_ACCESS_KEY
app.config['SQLALCHEMY_DATABASE_URI'] = DATA_BASE_URL
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
connect_db(app)

app.debug = False  # False to turn off FDT
debug = DebugToolbarExtension(app)


@app.get("/")
def home():
    """Displays homepage"""

    return render_template('home.html')


@app.get("/photos")
def photos():
    """Displays all active photos"""

    recent_photo = Photo.query.filter_by(active=True) \
        .order_by(Photo.id.desc()).first()

    if recent_photo == None:
        return render_template("photos.html", recent_photo=None, photos=None)
    photos = Photo.query.filter(Photo.id != recent_photo.id, Photo.active) \
        .order_by(func.random()).all()

    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    return render_template("photos.html",
                           photos=photos,
                           recent_photo=recent_photo,
                           timestamp=timestamp)


@app.route("/photos/<int:photo_id>", methods=["GET", "POST"])
def photo(photo_id):
    """Display active individual photo and handles edit form submissions"""

    photo = Photo.query.get_or_404(photo_id)

    if not photo.active:
        return render_template("notfound.html")

    form = EditPhotoForm(obj=photo)

    if form.validate_on_submit():
        # Gather form data
        photo.title = form.title.data
        photo.caption = form.caption.data
        if form.black_and_white.data:
            # Edit photo to B&W
            response = requests.get(photo.s3_photo_url_display)

            ind_of_slash = photo.s3_photo_url_display.rfind("/")
            file_name = photo.s3_photo_url_display[ind_of_slash + 1:]

            with open(f"./staging/{file_name}", "wb") as f:
                print("response.content", response.content)
                f.write(response.content)
            image = Image.open(f"./staging/{file_name}")
            image_bw = image.convert("L")
            image_bw.save(f"./staging/{file_name}")

            ind_of_slash = photo.s3_photo_url_display.rfind("/")
            file_name = photo.s3_photo_url_display[ind_of_slash + 1:]

            s3_upload(f"./staging/{file_name}", file_name)

            os.remove(f"./staging/{file_name}")
            photo.edited = True
            photo.black_and_white = True

        db.session.commit()
        flash("Edit Success!")

    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    return render_template("photo.html", photo=photo, form=form, timestamp=timestamp)

#
@app.route("/addphoto", methods=["GET", "POST"])
def add_photo():
    """Displays and handles add photo form"""

    form = AddPhotoForm()

    if form.validate_on_submit():
        form.file.data.save(f'./staging/{form.file.data.filename}')
        # Upload photo to S3 to retain an original copy so it can always be
        # referenced if edits need to be undone.
        s3_upload(
            f'./staging/{form.file.data.filename}',
            form.file.data.filename
        )
        # Upload photo to S3 that will be the display version of the photo
        s3_upload(
            f'./staging/{form.file.data.filename}',
            "display_" + form.file.data.filename
        )
        # After succesful upload, remove the photo from ondisk storage
        os.remove(f'./staging/{form.file.data.filename}')

        # Create photo object to save into db
        new_photo = Photo(
            title=form.title.data,
            caption=form.caption.data,
            active=True,
            edited=False,
            s3_photo_url_orig=f'{BASE_URL}/{form.file.data.filename}',
            s3_photo_url_display=f'{BASE_URL}/display_' +
            f'{form.file.data.filename}'
        )
        db.session.add(new_photo)
        db.session.commit()

        flash("Added successfuly!", "success")

        return redirect('/photos')

        # TODO: error handling?
        # TODO: Redirect back to photos with flashed message

    return render_template("add_photo.html", form=form)
