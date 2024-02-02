import os
from dotenv import load_dotenv
import boto3
from flask import Flask, redirect, flash, render_template, url_for
from flask_debugtoolbar import DebugToolbarExtension
from forms import AddPhotoForm, EditPhotoForm
import requests
from PIL import Image

from models import db, connect_db, Photo

load_dotenv()

AWS_ACCESS_KEY_ID = os.environ['AWS_ACCESS_KEY_ID']
AWS_SECRET_ACCESS_KEY = os.environ['AWS_SECRET_ACCESS_KEY']
S3_BUCKET = os.environ['S3_BUCKET']
BASE_URL = f'https://{S3_BUCKET}.s3.us-west-1.amazonaws.com'

app = Flask(__name__)
app.config['SECRET_KEY'] = AWS_SECRET_ACCESS_KEY
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get(
    "DATABASE_URL", 'postgresql:///saltly')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
connect_db(app)

app.debug = True  # False to turn off FDT
debug = DebugToolbarExtension(app)

@app.get("/")
def home():
    """Displays homepage"""

    redirect_url = url_for('photos')
    return redirect(redirect_url)

    # return render_template('home.html')

@app.get("/photos")
def photos():
    """Displays all active photos"""

    photos = Photo.query.filter_by(active=True).all()
    # TODO: Organize by newest? By descending ID or a timestamp?

    return render_template("photos.html", photos=photos)


@app.route("/photos/<int:photo_id>", methods=["GET", "POST"])
def photo(photo_id):
    """Display active individual photo and handles edit form submissions"""

    photo = Photo.query.get_or_404(photo_id)

    if photo.active == False:
        return render_template("notfound.html")

    form = EditPhotoForm(obj=photo)

    if form.validate_on_submit():
        # Gather form data
        photo.title = form.title.data
        photo.caption = form.caption.data
        if form.black_and_white.data == True:
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

            # Upload photo to S3
            s3 = boto3.client(
                "s3",
                "us-west-1",
                aws_access_key_id=AWS_ACCESS_KEY_ID,
                aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
            )

            # Uploading a file, WILL REPLACE/OVERWRITE IF SAME OBJECT KEY NAME
            ind_of_slash = photo.s3_photo_url_display.rfind("/")
            file_name = photo.s3_photo_url_display[ind_of_slash + 1:]

            s3.upload_file(
                # f"./staging/{photo.s3_photo_url_display}",
                f"./staging/{file_name}",
                S3_BUCKET,    # or saltly-bucket
                file_name
            )

            os.remove(f"./staging/{file_name}")
            # Update DB display url with S3 url SHOULD BE SAME URL!!!!
            # Update DB edited to True
            photo.edited = True
            photo.black_and_white = True
        # Commit to DB
        db.session.commit()
        # Create flash message
        flash("Edit Success!")

    return render_template("photo.html", photo=photo, form=form)



@app.route("/addphoto", methods=["GET", "POST"])
def add_photo():
    """Displays and hadles add photo form"""

    form = AddPhotoForm()

    if form.validate_on_submit():
        form.file.data.save(f'./staging/{form.file.data.filename}')

        s3 = boto3.client(
            "s3",
            "us-west-1",
            aws_access_key_id=AWS_ACCESS_KEY_ID,
            aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
        )

        # Uploading a file, WILL REPLACE/OVERWRITE IF SAME OBJECT KEY NAME
        s3.upload_file(
            f'./staging/{form.file.data.filename}',
            S3_BUCKET,    # or saltly-bucket
            form.file.data.filename
        )

        s3.upload_file(
            f'./staging/{form.file.data.filename}',
            S3_BUCKET,    # or saltly-bucket
            "display_" + form.file.data.filename
        )

        os.remove(f'./staging/{form.file.data.filename}')

        new_photo = Photo(
            title=form.title.data,
            caption=form.caption.data,
            active=True,
            edited=False,
            s3_photo_url_orig=f'{BASE_URL}/{form.file.data.filename}',
            s3_photo_url_display=f'{BASE_URL}/display_{form.file.data.filename}'
        )
        db.session.add(new_photo)
        db.session.commit()

        flash("Added successfuly!", "success")

        return redirect('/photos')

        # TODO: error handling?
        # TODO: Redirect back to photos with flashed message

    return render_template("add_photo.html", form=form)
