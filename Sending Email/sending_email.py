
import smtplib

sender = 'arjuneastkoleri2000@gmail.com'
receivers = ['gp6984575@gmail.com']

message = """From: From Person <from@fromdomain.com>
To: To Person <to@todomain.com>
MIME-Version: 1.0
Content-type: text/html
Subject: SMTP HTML e-mail test

This is an e-mail message to be sent in HTML format

<b>This is HTML message.</b>
<h1>This is headline.</h1>
"""

try:
   smtpObj = smtplib.SMTP('smtp.gmail.com',587)
   smtpObj.starttls()
   password=input(str("enter your password"))
   smtpObj.login('arjuneastkoleri2000@gmail.com',password)
   smtpObj.sendmail(sender, receivers, message)
   print("Successfully sent email")
except Exception:
   print("Error: unable to send email")