import math, random
import hashlib, binascii, os

from flask_mail import Mail, Message
from flask import current_app

from weather_api import query_api, query_advanced_api, get_local_time



def hash_password(password):
    salt = hashlib.sha256(os.urandom(60)).hexdigest().encode('ascii')
    pwdhash = hashlib.pbkdf2_hmac('sha512', password.encode('utf-8'), salt, 100000)
    pwdhash = binascii.hexlify(pwdhash)
    return (salt + pwdhash).decode('ascii')


def verify_password(stored_password, provided_password):
    salt = stored_password[:64]
    stored_password = stored_password[64:]
    pwdhash = hashlib.pbkdf2_hmac('sha512', provided_password.encode('utf-8'), 
                                  salt.encode('ascii'), 100000)
    pwdhash = binascii.hexlify(pwdhash).decode('ascii')
    return pwdhash == stored_password


def gen_otp(length):
    chars = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    otp = "" 
    for i in range(length): 
        otp += chars[math.floor(random.random() * len(chars))]
  
    return otp


def send_otp_via_mail(email, otp):
    mail = Mail(current_app)
    msg = Message("Registration OTP code", recipients=[email])
    msg.body = f"OTP for registration: {otp}"
    mail.send(msg)