import smtplib
from email.message import EmailMessage

email = EmailMessage()
email['from'] = 'Manfred'
email['to'] = 'manny1@dr.com'
email['subject'] = 'Testing my skills'

email.set_content('I am testing how to code. Hahaha')

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login('email@account.com', 'password')
    smtp.send_message(email)
    print('message sent')