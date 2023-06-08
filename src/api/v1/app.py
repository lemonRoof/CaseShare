#!/usr/bin/python3
from flask import Flask, jsonify, render_template
from flasgger import Swagger
from models import storage
from api.v1.views import api_views
from api.v1.views.decorators import token_required
from flasgger import Swagger

app = Flask(__name__)
app.register_blueprint(api_views)

@app.after_request
def add_cors_headers(response):
    response.headers.add("Access-Control-Allow-Origin", "*")
    response.headers.add("Access-Control-Allow-Headers", "Content-Type,Accepts,Authorization,x-token")
    response.headers.add("Access-Control-Allow-Methods", "GET,POST,PUT,DELETE")
    return response

app.config['SWAGGER'] = {
    'title': 'CaseShare Swagger API',
    'uiversion': 3
}
Swagger(app)

@app.get('/status', strict_slashes=False)
@token_required
def logInStatus(email):
    if storage.get_user_by_email(email):
        return jsonify({}), 200
    return jsonify({}), 404

@app.get('/home', strict_slashes=False)
@token_required
def home(email):
    """Return the homepage"""
    return render_template('home.html')

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5001, debug=True)
