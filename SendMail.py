#!/usr/bin/env python3
import smtplib, ssl, getpass

smtp_server = 'smtp.gmail.com'
port_number = 587
sender_email = input('Sender email address:')
reciever_email = input('Reciever email address:')
message = input('Message:')
sender_password = getpass.getpass()

context = ssl.create_default_context()
server = smtplib.SMTP(smtp_server, port_number)

try:
    server.ehlo()
    server.starttls(context=context)
    server.ehlo()
    server.login(sender_email, sender_password)
    server.sendmail(sender_email, reciever_email, message)
except Exception as ex:
    print(ex)
finally:
    server.quit()
