from flask import Flask, request, render_template
from flask_restful import Resource, Api, reqparse
from main import generate_video, input_flask
import os
from wtforms import Form, FloatField, validators
from math import pi

class InputForm(Form):
	ID0 = FloatField(
		label='required', default='Animals',
		validators=[validators.InputRequired()])
	ID1 = FloatField(
		label='required', default='Dogs',
		validators=[validators.InputRequired()])
	ID2 = FloatField(
		label='required', default='Cats',
		validators=[validators.InputRequired()])
	ID3 = FloatField(
		label='required', default='Penguins',
		validators=[validators.InputRequired()])

app = Flask(__name__)
api = Api(app)

@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', name=name)



@app.route('/', methods=['GET', 'POST'])
def index():
	form = InputForm(request.form)
	if request.method == 'POST':
		input_flask(form.ID0, form.ID1,
		form.ID2, form.ID3)
		generate_video()
		result = os.path.join('./static/','output.mp4')
	else:
		result = None

	return render_template('req.html',
		form=form, result=result)

		

#api.add_resource(media, '/')

if __name__ == '__main__':
	app.run(debug=True)