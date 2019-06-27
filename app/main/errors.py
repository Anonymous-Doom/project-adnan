from flask import render_template
from . import main

#
# Error Handler Routes below [404]
#

@main.app_errorhandler(404)                     #use main blueprint to route 404 responses
def page_not_found(e):
    return render_template('404.html'), 404     