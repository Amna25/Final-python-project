from flask import Flask, render_template

from controllers.cities_controller import cities_blueprint
from controllers.countries_controller import countries_blueprint
from controllers.destinations_controller import destinations_blueprint
application = Flask(__name__)
app = application

app.register_blueprint(cities_blueprint)
app.register_blueprint(countries_blueprint)
app.register_blueprint(destinations_blueprint)

@application.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    application.run(debug=True)