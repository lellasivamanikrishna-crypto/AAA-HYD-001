import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

sender = "loyola.sivamanikrishna.@gmail.com"
password = input("Enter your password?")

recipients = [
    "sivamani2006@gmail.com",
    "lellasivamanikrishna@gmail.com",
    "sivamani@student.rvit.edu"
]

subject = "Test Mail"
message = "This is a Test mail, Please Ignore it"

server = smtplib.SMTP("smtp.gmail.com", 587)
server.starttls()
server.login(sender, password)

print("Login Successful")

for recipient in recipients:
    msg = MIMEMultipart()
    msg["From"] = sender
    msg["To"] = recipient
    msg["Subject"] = subject

    msg.attach(MIMEText(message, "plain"))

    server.sendmail(sender, recipient, msg.as_string())

server.quit()
print("All emails sent successfully.")
