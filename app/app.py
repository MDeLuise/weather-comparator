from flask import Flask, jsonify, request, render_template, redirect
from flask_jwt_extended import JWTManager
from flask_mail import Mail
from flask_mongoengine import MongoEngine, MongoEngineSessionInterface
from flask_debugtoolbar import DebugToolbarExtension

from weather_api import get_local_time, query_api, query_advanced_api
from views.token import token
from views.api import api
from views.index import index





app = Flask(__name__)
app.config.from_object("config.ProductionConfig")


app.register_blueprint(index)
app.register_blueprint(api)
app.register_blueprint(token)

jwt = JWTManager(app)

db = MongoEngine()
db.init_app(app)

app.session_interface = MongoEngineSessionInterface(db)
toolbar = DebugToolbarExtension(app)
toolbar.init_app(app) 





if __name__ == "__main__":
    app.run(host='0.0.0.0')