from src import api
from src.resources.actors import ActorListApi
from src.resources.books import BookListApi
from src.resources.smoke import Smoke

api.add_resource(Smoke, '/smoke', strict_slashes=False)
api.add_resource(BookListApi, '/books', '/books/<uuid>', strict_slashes=False)
api.add_resource(ActorListApi, '/actors', '/actors/<uuid>', strict_slashes=False)
