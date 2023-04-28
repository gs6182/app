import smtplib

sender_email = "bachirakarno@gmail.com"
rec_email = "aryakesharwani1234@gmail.com"
password = input("please enter your password: ")
message = "hey this was sent using python"

server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(sender_email, password)
print("login success")
server.sendmail(sender_email, rec_email, message)
print("Email has been sent to ", rec_email)
