from flask import Flask, request, Blueprint,jsonify, current_app
from flask_mail import Mail, Message


mail_routes= Blueprint('mail',__name__)
mail = Mail()


@mail_routes.route('/send-email', methods=['GET', 'POST'])
def home():
    receiver_email = request.json.get('receiver_email')
    print(receiver_email)
    # Create a message object
    if request.method =='POST':
        
        msg = Message('Hello from Flask', 
                  sender='honeykarnot@gmail.com', 
                  recipients=[receiver_email])
        msg.body = 'This is a test email sent from a Flask app using Flask-Mail!'
        # Send the message
        mail.send(msg)
    return jsonify({"message":"mail sent"})