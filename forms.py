from flask_wtf import FlaskForm

from wtforms import StringField, FileField, BooleanField

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
        validators=[InputRequired()]  # TODO: restrict type of file / SIZING?
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
        "noir mode",
        validators=[Optional()]
    )
