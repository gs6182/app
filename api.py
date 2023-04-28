from flask import Flask, request, jsonify, render_template
from flask_mail import Mail, Message
import os
import pandas as pd

app = Flask(__name__,template_folder='templates')
mail = Mail(app)


#Configure mail settings
# app.config['MAIL_SERVER'] = 'smtp.gmail.com'
# app.config['MAIL_PORT'] = 587
# app.config['MAIL_USE_TLS'] = True
# app.config['MAIL_USERNAME'] = 'your-email@gmail.com'
# app.config['MAIL_PASSWORD'] = 'your-email-password'


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    # Get the uploaded file
    file = request.files['file']

    # Get the folder path where the file should be saved
    folder_path = 'E:\\nunu\server\\montly\\'

    # Save the file to the folder
    file.save(folder_path + file.filename)

    return 'File uploaded successfully'



@app.route('/analyze_expenses', methods=['GET'])
def analyze_expenses_api():
    # Get the folder path from the request
    # folder_path = request.json.get('folder_path')
    folder_path = 'E:\\nunu\server\\montly\\'

    # budget =  request.json.get('budget')
    # alert_email=request.json.get('alert_email')

    # Create an empty dictionary to store the results for each category
    category_totals = {}
    category_monthly_totals = {}

    # Create an empty list to store the total expenditures for each month
    monthly_totals = []

    # Get the list of files in the folder
    file_list = os.listdir(folder_path)
    print(file_list)

    # Loop through each file in the folder
    for file_name in file_list:
        if file_name.endswith('.csv'):
            file_path = os.path.join(folder_path, file_name)
            # Read the CSV file into a pandas DataFrame
            df = pd.read_csv(file_path)

            # Extract the month from the file name
            month = file_name.split('.')[0].capitalize()

            # Loop through each row in the DataFrame
            for index, row in df.iterrows():
                # Extract the category and amount for the current row
                category = row['Category']
                amount = row['Amount']

                # Check if the category already exists in the dictionary
                if category in category_totals:
                    # If it does, add the current amount to the existing total
                    category_totals[category] += amount
                    if month in category_monthly_totals[category]:
                        category_monthly_totals[category][month] += amount
                    else:
                        category_monthly_totals[category][month] = amount
                else:
                    # If it doesn't, create a new key with the current amount as the value
                    category_totals[category] = amount
                    category_monthly_totals[category] = {month: amount}

            # Calculate the total expenditure for the current month and add it to the list
            monthly_total = sum(df['Amount'])
            monthly_totals.append((month, monthly_total))

    # Calculate the total and average expenditures for each category
    total_by_category = sum(category_totals.values())
    average_by_category = total_by_category / len(category_totals)

    # Check if the average spending exceeds the budget
    # budget=1000
    # if average_by_category > budget:
        # Create a message object
        # msg = Message(subject='Budget Alert', recipients=[alert_email])
        # msg.body = f"Your average spending for the month exceeded your budget of {budget}."
        
        # Send the message
        # mail.send(msg)

    # Create a dictionary with the results
    results = {
        "total_by_category": category_totals,
        "total_expenditure_for_all_months": total_by_category,
        "average_expenditure_per_category": average_by_category,
        "total_expenditure_by_category_per_month": category_monthly_totals,
        # "average_expenditure_per_category_per_month": {category: sum(monthly_totals[category].values()) / len(monthly_totals[category]) for category in category_monthly_totals},
        "total_expenditure_by_month": {month: total for month, total in monthly_totals}
    }

    # Return the results as JSON
    return jsonify(results)

if __name__ == '__main__':
    app.run(debug=True)
