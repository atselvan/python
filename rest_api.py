"""
Simple REST API Example + Documentation with flask and flask-restplus
"""

from http import HTTPStatus
from http.client import responses
from flask import Flask
from flask_restplus import Resource, Api, fields

authorizations = {
    'basic': {
        'type': 'basic',
        'in': 'header',
        'name': 'AUTHORIZATION'
    }
}

app = Flask(__name__)
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True
api = Api(app,
          title='Book Store API',
          version='1.0.0',
          description='API to manage a catalog of books',
          contact="Allan Tony Selvan",
          contact_email="books@privatesquare.in",
          contact_url="htt://books.privatesquare.in",
          authorizations=authorizations,
          security="basic",
          scheme=["http", "https"],
          ordered=True)

app_ns = api.namespace('books', description='Books operations')

resp_model = api.model('Response', {
    'message': fields.String
})

err_resp_model = api.model('ErrResponse', {
    'error': fields.String
})


@app_ns.route("/")
class BooksApi(Resource):

    @app_ns.response(HTTPStatus.OK, responses[HTTPStatus.OK], resp_model)
    @app_ns.response(HTTPStatus.BAD_REQUEST, responses[HTTPStatus.BAD_REQUEST], err_resp_model)
    @app_ns.response(HTTPStatus.CONFLICT, responses[HTTPStatus.CONFLICT], err_resp_model)
    @app_ns.response(HTTPStatus.INTERNAL_SERVER_ERROR, responses[HTTPStatus.INTERNAL_SERVER_ERROR], err_resp_model)
    def get(self):
        """
        Get book records
        :return:
        """
        return {"message": "Get some books"}

    @app_ns.response(HTTPStatus.CREATED, responses[HTTPStatus.CREATED], resp_model)
    @app_ns.response(HTTPStatus.BAD_REQUEST, responses[HTTPStatus.BAD_REQUEST], err_resp_model)
    @app_ns.response(HTTPStatus.CONFLICT, responses[HTTPStatus.CONFLICT], err_resp_model)
    @app_ns.response(HTTPStatus.INTERNAL_SERVER_ERROR, responses[HTTPStatus.INTERNAL_SERVER_ERROR], err_resp_model)
    def post(self):
        """
        Create a new book record
        :return:
        """
        return {"message": "Created a new book record"}

    @app_ns.response(HTTPStatus.NO_CONTENT, responses[HTTPStatus.NO_CONTENT], resp_model)
    @app_ns.response(HTTPStatus.BAD_REQUEST, responses[HTTPStatus.BAD_REQUEST], err_resp_model)
    @app_ns.response(HTTPStatus.CONFLICT, responses[HTTPStatus.CONFLICT], err_resp_model)
    @app_ns.response(HTTPStatus.INTERNAL_SERVER_ERROR, responses[HTTPStatus.INTERNAL_SERVER_ERROR], err_resp_model)
    def delete(self):
        """
        Delete a book record
        :return:
        """
        return {"message": "Deleted an existing book record"}


if __name__ == "__main__":
    app.run()
