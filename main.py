from flask import Flask
from flask import render_template

app= Flask(__name__)

app.run(debug= True, port=8000)