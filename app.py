from flask import Flask, render_template, jsonify
import openai
from config import key

openai.api_key = key
app = Flask(__name__)


@app.route('/')
def index():
  return render_template('main.html', )


@app.route('/generateimages/<prompt>')
def generateImage(prompt):
  print("prompt: ", prompt)
  response = openai.Image.create(prompt=prompt, n=3, size="1024x1024")
  return jsonify(response)


app.run(host='0.0.0.0', port=81)
