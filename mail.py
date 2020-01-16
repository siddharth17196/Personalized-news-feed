import smtplib
import os
from email.message import EmailMessage
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

email_addr = 'shizzlenfizzle@gmail.com'
password = 'siddupiddu'
reciever = 'siddharthnair49@gmail.com'

msg = MIMEMultipart("alternative")
# msg = EmailMessage()
msg['Subject'] = 'NEWZZ UPDATE'
msg['From'] = email_addr
msg['To'] = reciever
# msg.set_content('')

# Create the plain-text and HTML version of your message
text = """\
Hi,
How are you?
Real Python has many great tutorials:
www.realpython.com"""
html = """\
<html>
  <body>
	<p>Hi,<br>
	   How are you?<br>
	   <a href="http://www.realpython.com">Real Python</a> 
	   has many great tutorials.
	</p>
  </body>
</html>
"""

# Turn these into plain/html MIMEText objects
part1 = MIMEText(text, "plain")
part2 = MIMEText(html, "html")

# Add HTML/plain-text parts to MIMEMultipart message
# The email client will try to render the last part first
msg.attach(part1)
msg.attach(part2)

# Create secure connection with server and send email
with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
	smtp.login(email_addr, password)
	smtp.send_message(msg)	