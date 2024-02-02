from flask_wtf import FlaskForm

from wtforms import StringField, FileField, BooleanField

from wtforms.validators import InputRequired, Optional, Length

# def file_type_check(form, field):
#     """Checks input file type against accepted file types"""

#     if field.data
# TODO: Validate file type.


class AddPhotoForm(FlaskForm):
    """Add Photo Form"""

    title = StringField(
        "Title",
        validators=[InputRequired(), Length(max = 55)]
    )

    caption = StringField(
        "Caption",
        validators=[InputRequired(), Optional()]
    )

    file = FileField(
        "Photo File",
        validators=[InputRequired()] #TODO: Add options to restrict type of file / SIZING?
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
