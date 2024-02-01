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

    photos = Photo.query.filter_by(active=True).all() #TODO: Organize by newest? By descending ID or a timestamp?

    return render_template("photos.html", photos=photos)


@app.get("/photos/<int:photo_id>")
def photo(photo_id):
    """Display active individual photo"""

    photo = Photo.query.get_or_404(photo_id)

    if photo.active:
        return render_template("photo.html", photo=photo)

    return render_template("notfound.html")



@app.route("/addphoto", method=["GET", "POST"])
def add_photo():
    """Displays and hadles add photo form"""

    form = AddPhotoForm()

    if form.validate_on_submit():
        # Gather all form info
        title = form.title.data
        caption = form.caption.data
        file = form.file.data
        print(file)
        # Add photo to S3, can this return an error???
        # Add to db via ORM
        # Redirect back to photos with flashed message

    return render_template("add_photo.html", form=form)
