""" Models for saltly """

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Photo(db.Model):
    """ Photos model """

    __tablename__ = 'photos'

    id = db.Column(
        db.Integer,
        primary_key=True,
        autoincrement=True)

    title = db.Column(
        db.String(300),
        nullable=False
    )

    caption = db.Column(
        db.String(700),
        nullable=False  # TODO: Add a default value of None?
    )

    s3_photo_url = db.Column(
        db.String(700),
        nullable=False
    )

    active = db.Column(
        db.Boolean,
        nullable=False,
        default=True,
    )

    # s3_thumbnail_url = db.Column(
    #     db.String(700),
    #     nullable=False
    # )

    # exif_data = db.Column(
    #     db.String(1000)
    # )


def connect_db(app):
    """
    Connect this database to provided Flask app.
    """

    app.app_context().push()
    db.app = app
    db.init_app(app)
