import json, sys
from pprint import pprint as pp

from flask import jsonify, request, render_template, redirect, Blueprint
from flask_jwt_extended import jwt_required, get_jwt_identity, jwt_optional
import flask_mongoengine
from flask_mongoengine import ValidationError

from common import gen_otp, send_otp_via_mail, hash_password, verify_password
from weather_api import query_api, query_advanced_api, get_local_time
from models import User


api = Blueprint('api', __name__)




@api.route('/api/compare', methods=['POST', 'GET'])
@jwt_optional
def compare():
    data = []
    error = None
    advanced_data = None

    city1 = request.values.get("city1")
    city2 = request.values.get("city2")
    if (request.method == "POST" or (city1 and city2)):
        for city in (city1, city2):
            resp = query_api(city)
            pp(resp)
            if resp:
                data.append(resp)
        if len(data) != 2:
            error = 'Did not get complete response from Weather API'

        if get_jwt_identity():
            advanced_data = []
            for city in (city1, city2):
                resp = query_advanced_api(city)
                pp(resp)
                if resp:
                    advanced_data.append(resp)

    return render_template("weather.html", data=data, error=error,
        time=get_local_time, adv_data=advanced_data)
        


@api.route('/api/login', methods=['POST', 'GET'])
@jwt_optional
def login_page():
    if not get_jwt_identity():
        data = {"signup": request.args.get('signup', default=False)}
        return render_template('login.html', data=data)
    else:
        return redirect("/api/compare")


@api.route('/api/signup', methods=['POST'])
def signup():
    email = request.values.get('email')
    password = request.form.get('password')
    otp = gen_otp(6)
    send_otp_via_mail(email, otp)

    if User.objects(email=email):
        return json.dumps(obj={"signup": False, "error": "email already registred"}), 400

    try:
        User(email=email, password=hash_password(password), otp=otp).save()
    except ValidationError:
        return json.dumps(obj={"signup": False, "error": "email not valid"}), 400   

    return json.dumps(obj={"signup": True, "otp": otp}), 200


@api.route('/api/create_user', methods=['POST'])
def create_user():
    email = request.form.get('username')
    password = request.form.get('password')
    otp = request.form.get('otp')
    
    user = User.objects(email=email, otp=otp).first()
    if user and verify_password(user.password, password): # for not allow creating user easily
        user.update(conf=True)
        return jsonify({'register': True}), 200

    else:
        return jsonify({'register': False}), 401


@api.route('/api/example', methods=['GET'])
@jwt_required
def protected():
    username = get_jwt_identity()
    return jsonify({'hello': 'from {}'.format(username)}), 200