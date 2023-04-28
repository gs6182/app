from flask import Flask, render_template, request
from flask_mail import Mail, Message
import os


app = Flask(__name__,template_folder='templates')
#Configure mail settings
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
app.config['MAIL_USERNAME'] = 'honeykarnot@gmail.com'
app.config['MAIL_PASSWORD'] = 'tnhudufymszxmmgi'

mail = Mail(app)

@app.route('/send-email', methods=['GET', 'POST'])
@app.route('/', methods=['GET', 'POST'])
def home():
    # Create a message object
    if request.method =='POST':
        msg = Message('Hello from Flask', 
                  sender='honeykarnot@gmail.com', 
                  recipients=['karnotgaurav@gmail.com'])
        msg.body = 'This is a test email sent from a Flask app using Flask-Mail!'
        # Send the message
        mail.send(msg)
        return "sent email"
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
