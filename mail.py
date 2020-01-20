import smtplib
import os
from email.message import EmailMessage
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import scrap

news = scrap.start()

details = []
with open('confidential.txt','r') as f:
	for x in f:
		details.append(x)
email_addr = details[0][6:-1]
password = details[1][6:-1]
reciever = details[2][6:-1]
# email_addr = 'shizzlenfizzle@gmail.com'
# password = 'siddupiddu'
# reciever = 'siddharthnair49@gmail.com'

nws = ''
for i in range(len(news.head)):
	nws += '***********************************************************************************\n'
	for h, l in zip(news.head[i], news.link[i]):
		nws += str(h)+"--->"+'('+str(l)+')'+'\n'

# msg = MIMEMultipart("alternative")
msg = EmailMessage()
msg['Subject'] = 'NEWZZ UPDATE'
msg['From'] = email_addr
msg['To'] = reciever
msg.set_content(nws)

# Create the plain-text and HTML version of your message

# html = """\
# <!DOCTYPE html>
# <html>
# 	<body>
# 	<p>Hi,<br>
# 		How are you?<br>
# 		<a href="http://www.realpython.com">Real Python</a>
# 		has many great tutorials.
# 		<ul>
# 			{% for elem in f %}
# 			<li>{{ elem }}</li>
# 			{% endfor %}
# 		</ul>
# 	</p>
# 	</body>
# </html>
# """
# msg.add_alternative(html, subtype='html')
# Turn these into plain/html MIMEText objects
# part1 = MIMEText(text, "plain")
# part2 = MIMEText(html, "html")

# Add HTML/plain-text parts to MIMEMultipart message
# The email client will try to render the last part first
# msg.attach(part1)
# msg.attach(part2)

# Create secure connection with server and send email
with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
	smtp.login(email_addr, password)
	smtp.send_message(msg)
