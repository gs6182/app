from flask import Flask, render_template, request, jsonify
from flask_mail import Mail, Message

app = Flask(__name__, template_folder='templates')

# Configure mail settings
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
app.config['MAIL_USERNAME'] = 'honeykarnot@gmail.com'
app.config['MAIL_PASSWORD'] = 'tnhudufymszxmmgi'

mail = Mail(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload')
def upload_data():
    return render_template('upload.html')

@app.route('/result')
def show_result():
    return render_template('result.html')

@app.route('/pie')
def show_pie():
    return render_template('piechat.html')

@app.route('/send-email', methods=['POST'])
def send_email():
    receiver_email = request.json.get('receiver_email')
    if not receiver_email:
        return jsonify({'error': 'Missing parameter: receiver_email'})
    msg = Message('THANK YOU FOR REGISTERING WITH US',
                  sender='honeykarnot@gmail.com',
                  recipients=[receiver_email])
    msg.body = 'YOU HAVE REGISTERED FOR OUR MONEY MANAGEMENT PROJECT'
    mail.send(msg)
    return jsonify({'message': 'Mail sent'})

from api2 import api_routes
app.register_blueprint(api_routes)

if __name__ == '__main__':
    app.run(debug=True)
