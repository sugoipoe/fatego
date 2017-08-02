# landing page
from flask import Blueprint, render_template

landing = Blueprint('landing', __name__)

@landing.route('/')
def landing_page():
  # Do some stuff
  return render_template('landing/index.html')
