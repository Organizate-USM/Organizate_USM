from flask import Flask
from flask import render_template

import forms

app = Flask(__name__)

@app.route('/')
def index():
    comment_form = forms.CommentForm()
    title = "Organizate USM"
    return render_template('index.html', title=title, form=comment_form)

if __name__ == '__main__':
    app.run(debug=True, port=8000)
