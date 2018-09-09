import random
import os

from flask import Flask, render_template

with open('lines.txt', 'r') as f:
	lines = list(set(f.readlines()))

emoticons = '☺ ☻ ✌ ☹ ♡ ♥ ❤ ⚘ ❀ ❃ ❁ ✼ ☀ ✌ ♫ ♪ ☃ ❄ ❅ ❆'

def get_line():
	line = random.choice(lines).strip()
	sel = random.random() 
	if sel < 0.1:
		return 'שנה טובה ומתוקה'

	if sel < 0.3:
		return '<b>' + line + '</b>'

	if sel < 0.5:
		return line + ' ' + random.choice(emoticons)
	return line

def make_greeting(length=None):
	if length is None:
		length = random.randrange(4, 30) * 2

	return '<br>'.join(get_line() for x in range(length))



app = Flask(__name__)


@app.route('/')
def hello():
	return render_template('index.html', greeting=make_greeting())


if __name__ == '__main__':
	app.run(port=int(os.environ.get('PORT') or '8001'), host='0.0.0.0', debug=True)

