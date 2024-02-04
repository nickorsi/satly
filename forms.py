from flask_wtf import FlaskForm

from flask_wtf.file import FileAllowed, FileSize

from wtforms import StringField, FileField, BooleanField, RadioField

from wtforms.validators import InputRequired, Optional, Length


class AddPhotoForm(FlaskForm):
    """Add Photo Form"""

    title = StringField(
        "Title",
        validators=[InputRequired(), Length(max=55)]
    )

    caption = StringField(
        "Caption",
        validators=[InputRequired(), Optional()]
    )

    file = FileField(
        "Photo File",
        validators=[
            InputRequired(),
            FileAllowed(['jpg', 'jpeg', 'png'], "Only Jpeg or PNG allowed!"),
            FileSize(15000)
        ]
    )


class EditPhotoForm(FlaskForm):
    """Add Photo Form"""

    title = StringField(
        "Title",
        validators=[InputRequired(), Length(max=55)]
    )

    caption = StringField(
        "Caption",
        validators=[InputRequired(), Optional()]
    )

    black_and_white = BooleanField(
        "Noir Mode",
        validators=[Optional()]
    )

    # color_pallet = RadioField(
    #     "Color Pallets",
    #     validators=[InputRequired()],
    #     choices=[("orig", "Original"), ("black_and_white", "Noir Mode")],
    #     default= "orig"
    # )

    # TODO: Incorporate the above radiofield to display in the the form, must
    # iterate in the jinja template to avoid showing as a bulleted list. May
    # change DB to reflect what color pallet is chosen to help with displaying
    # defaults.