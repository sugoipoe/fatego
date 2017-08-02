from flask import Flask
from .views.landing import landing

app = Flask(__name__)
app.config.from_object('config')
app.register_blueprint(landing)


@app.route('/')
def launch():
  """
   TODO: Check out real docstring stuff
   The root route will show a basic page i.e. news, updates in the future
  """
  return 'Hello, World!'


