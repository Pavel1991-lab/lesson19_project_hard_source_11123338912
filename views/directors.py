from flask_restx import Resource, Namespace
from flask import request
from dao.model.director import DirectorSchema
from implemented import director_service
from utils import auth_required, admin_required

director_ns = Namespace('directors')


@director_ns.route('/')
class DirectorsView(Resource):

    def get(self):
        rs = director_service.get_all()
        res = DirectorSchema(many=True).dump(rs)
        return res, 200


    def post(self):
        req_json = request.json
        director_service.create(req_json)
        return "", 201


@director_ns.route('/<int:rid>')
class DirectorView(Resource):
    def get(self, rid):
        r = director_service.get_one(rid)
        sm_d = DirectorSchema().dump(r)
        return sm_d, 200


    def put(self, bid):
        req_json = request.json
        if "id" not in req_json:
            req_json["id"] = bid
        director_service.update(req_json)
        return "", 204


    def delete(self, bid):
        director_service.delete(bid)
        return "", 204


