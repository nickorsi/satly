import os
from dotenv import load_dotenv
import boto3
from flask import Flask, redirect, render_template
from flask_debugtoolbar import DebugToolbarExtension
from forms import AddPhotoForm

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
connect_db(app)

app.debug = True  # False to turn off FDT
debug = DebugToolbarExtension(app)


# trying to test boto3. ... fn to get object here.

# s3 = boto3.client(
#     "s3",
#     "us-west-1",
#     aws_access_key_id=AWS_ACCESS_KEY_ID,
#     aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
# )
# Uploading a file, WILL REPLACE/OVERWRITE IF SAME OBJECT KEY NAME
# s3.upload_file(
#     './static/Konica_Minolta_DiMAGE_Z3.jpg',
#     S3_BUCKET,    # or saltly-bucket
#     'Konica_Minolta_DiMAGE_Z3.jpg'
# )

# Get URL in S3, which will be BASE_URL + the object key (filename)


@app.get("/")
def home():
    """Displays homepage"""

    return render_template("home.html")


@app.get("/photos")
def photos():
    """Displays all active photos"""

    photos = Photo.query.filter_by(active=True).all()
    # TODO: Organize by newest? By descending ID or a timestamp?

    return render_template("photos.html", photos=photos)


@app.get("/photos/<int:photo_id>")
def photo(photo_id):
    """Display active individual photo"""

    photo = Photo.query.get_or_404(photo_id)

    if photo.active:
        return render_template("photo.html", photo=photo)

    return render_template("notfound.html")


@app.route("/addphoto", methods=["GET", "POST"])
def add_photo():
    """Displays and hadles add photo form"""

    form = AddPhotoForm()

    if form.validate_on_submit():

        s3 = boto3.client(
            "s3",
            "us-west-1",
            aws_access_key_id=AWS_ACCESS_KEY_ID,
            aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
        )

        s3.upload_file(form.file.data, S3_BUCKET, form.file.data)

        new_photo = Photo(
            title=form.title.data,
            caption=form.caption.data,
            active=True,
            # s3_photo_url=form.file.data
            s3_photo_url=f'{BASE_URL}/{form.file.data}'
        )
        # file gives a string of the filename
        #
        db.add(new_photo)
        db.commit()
        # Add photo to S3, can this return an error???
        # Add to db via ORM
        # Redirect back to photos with flashed message

    return render_template("add_photo.html", form=form)
