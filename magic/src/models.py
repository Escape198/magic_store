import uuid

from src import db


class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    release_date = db.Column(db.Date, index=True, nullable=False)
    uuid = db.Column(db.String(36), unique=True)
    description = db.Column(db.Text)
    distributed_by = db.Column(db.String(128), nullable=False)
    pages = db.Column(db.Integer)
    rating = db.Column(db.Float)

    def __init__(self, title, release_date, description, distributed_by, pages, rating):
        self.title = title
        self.release_date = release_date
        self.uuid = str(uuid.uuid4())
        self.description = description
        self.distributed_by = distributed_by
        self.pages = pages
        self.rating = rating

    def __repr__(self):
        return f'Book({self.title}, {self.release_date}, {self.uuid}, {self.distributed_by})'

    def to_dict(self):
        return {
            'title': self.title,
            'uuid': self.uuid,
            'release_date': self.release_date.strftime('%Y-%m-%d'),
            'distributed_by': self.distributed_by,
            'description': self.description,
            'pages': self.pages,
            'rating': self.rating,
        }
