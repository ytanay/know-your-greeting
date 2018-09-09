import random
import os

from flask import Flask, render_template

with open('lines.txt', 'r') as f:
	lines = list(set(f.readlines()))

emoticons = '☺ ☻ ✌ ☹ ♡ ♥ ❤ ⚘ ❀ ❃ ❁ ✼ ☀ ✌ ♫ ♪ ☃ ❄ ❅ ❆'
opening = ['לכבוד השנה החדשה', 'עם כניסת השנה החדשה', 'ובבוא השנה החדשה', 'יחד אל השנה החדשה', 'אספר לכם סיפור על השנה החדשה', 'נצעד אל פתח השנה החדשה', 'אין כמו שנה חדשה', 'רק היום נכנסת השנה']

def format_line(line):
	sel = random.random()

	if sel < 0.3:
		return '<b>' + line + '</b>'

	if sel < 0.5:
		return line + ' ' + random.choice(emoticons)
	return line

def make_greeting(length=None):
	all_lines = list(lines)

	random.shuffle(all_lines)

	if length is None:
		length = random.randrange(4, 30) * 2

	return random.choice(opening) + ',<br/>' + '<br>'.join(format_line(all_lines.pop().strip()) for x in range(length))



app = Flask(__name__)


@app.route('/')
def hello():
	return render_template('index.html', greeting=make_greeting())


if __name__ == '__main__':
	app.run(port=int(os.environ.get('PORT') or '8001'), host='0.0.0.0', debug=True)

