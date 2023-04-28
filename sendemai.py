from flask import flask, render_template

app = flask(__name__)

@app.route('home')
@app.route('/')
def home():
    return render_template('mail.html')



if __name__=='main':
    app.run(debug=True)