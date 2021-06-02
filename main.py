from flask import Flask, render_template

import datetime
import requests

app = Flask(__name__)


@app.route('/')
def welcome():
    now = datetime.datetime.now()
    curr_year = now.year
    return render_template('welcome.html', year=curr_year)


@app.route('/<name>')
def hi(name=None):

    response = requests.get(f'https://api.genderize.io?name={name}')
    response_dict = response.json()
    person_name = response_dict['name']
    person_gender = response_dict['gender']
    probability = response_dict['probability']
    return render_template('index.html', name=person_name.capitalize(), gender=person_gender, probability=probability)

if __name__ == '__main__':
    app.run(debug=True)
