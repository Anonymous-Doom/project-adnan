from flask import Blueprint

main = Blueprint('main',__name__)           #Instantiate "Main" blueprint for application

from . import views, errors                 #Import views and errors after defining main blueprint (avoid circular imports)