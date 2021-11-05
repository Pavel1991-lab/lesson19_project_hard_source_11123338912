from flask_restx import Resource, Namespace
from flask import request
from dao.model.director import DirectorSchema
from dao.model.favorite import Favorite_movieSchema
from implemented import director_service, favorite_service
from utils import auth_required, admin_required

favorite_ns = Namespace('favorite')





@favorite_ns.route('/')
class FavoriteView(Resource):

    def get(self):
        rs = favorite_service.get_all()
        res = Favorite_movieSchema(many=True).dump(rs)
        return res, 200


    def post(self):
        req_json = request.json
        favorite_service.create(req_json)
        return "", 201


@favorite_ns.route('/<int:rid>')
class DirectorView(Resource):
    def get(self, rid):
        r = favorite_service.get_one(rid)
        sm_d = Favorite_movieSchema().dump(r)
        return sm_d, 200

    def delete(self, bid):
        favorite_service.delete(bid)
        return "", 204