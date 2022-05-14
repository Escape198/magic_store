import datetime

from flask import request
from flask_restful import Resource

from src import api, db
from src.models import Book


class Smoke(Resource):
    def get(self):
        return {'message': 'OK'}


class BookListApi(Resource):

    def get(self, uuid=None):
        if not uuid:
            Books = db.session.query(Book).all()
            return [f.to_dict() for f in books], 200
        book = db.session.query(Book).filter_by(uuid=uuid).first()
        if not book:
            return "", 404
        return book.to_dict(), 200

    def post(self):
        book_json = request.json
        if not book_json:
            return {'message': 'Wrong data'}, 400
        try:
            book = Book(
                title=book_json['title'],
                release_date=datetime.datetime.strptime(book_json['release_date'], '%B %d, %Y'),
                distributed_by=book_json['distributed_by'],
                rating=book_json.get('rating'),
                pages=book_json.get('pages'),
                description=book_json.get('description')
            )
            db.session.add(book)
            db.session.commit()
        except (ValueError, KeyError):
            return {'message': 'Wrong data'}, 400
        return {'message': 'Created successfully', 'uuid': book.uuid}, 201

    def put(self, uuid):
        book_json = request.json
        if not book_json:
            return {'message': 'Wrong data'}, 400
        try:
            db.session.query(Book).filter_by(uuid=uuid).update(
                dict(
                    title=book_json['title'],
                    release_date=datetime.datetime.strptime(book_json['release_date'], '%B %d, %Y'),
                    distributed_by=book_json['distributed_by'],
                    rating=book_json.get('rating'),
                    pages=book_json.get('pages'),
                    description=book_json.get('description')
                )
            )
            db.session.commit()
        except (ValueError, KeyError):
            return {'message': 'Wrong data'}, 400
        return {'message': 'Updated successfully'}, 200

    def patch(self, uuid):
        book = db.session.query(Book).filter_by(uuid=uuid).first()
        if not book:
            return "", 404
        book_json = request.json
        title = book_json.get('title')
        release_date = datetime.datetime.strptime(book_json.get('release_date'), '%B %d, %Y') if book_json.get(
            'release_date') else None
        distributed_by = book_json.get('distributed_by'),
        rating = book_json.get('rating'),
        pages = book_json.get('pages'),
        description = book_json.get('description')

        if title:
            book.title = title
        elif release_date:
            book.release_date = release_date
        elif distributed_by:
            book.distributed_by = distributed_by
        elif rating:
            book.rating = rating
        elif pages:
            book.pages = pages
        elif description:
            book.description = description

        db.session.add(book)
        db.session.commit()
        return {'message': 'Updated successfully'}, 200

    def delete(self, uuid):
        book = db.session.query(Book).filter_by(uuid=uuid).first()
        if not book:
            return "", 404
        db.session.delete(book)
        db.session.commit()
        return '', 204


class ActorListApi(Resource):
    def get(self, uuid=None):
        pass

    def post(self):
        pass

    def put(self, uuid):
        pass

    def delete(self, uuid):
        pass


api.add_resource(Smoke, '/smoke', strict_slashes=False)
api.add_resource(BookListApi, '/books', '/books/<uuid>', strict_slashes=False)
api.add_resource(ActorListApi, '/actors', '/actors/<uuid>', strict_slashes=False)
