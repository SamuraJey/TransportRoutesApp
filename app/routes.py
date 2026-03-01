from flask import Blueprint

bp = Blueprint("main", __name__)

print("Importing auth")
from . import auth

print("Importing profile")
from . import profile

print("Importing route_management")
from . import route_management

print("All modules imported")
