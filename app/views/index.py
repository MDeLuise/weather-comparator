from flask import Blueprint, render_template, redirect, request
import requests

index = Blueprint('index', __name__)


@index.route('/', methods=['POST', 'GET'])
def home():
    return render_template("weather.html")