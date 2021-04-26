# Python code to illustrate Sending mail from
# your Gmail account
import smtplib

# creates SMTP session
s = smtplib.SMTP('smtp.gmail.com', 587)

# start TLS for security
s.starttls()

# Authentication
s.login("", "") # s.login("<Email-ID>", "<Password>")

# message to be sent
from email.message import EmailMessage



msg = EmailMessage()
cnt = """ """ # Message Content
msg.set_content(cnt)

msg['Subject'] = '' # <Subject of Mail>
msg['From'] = "" # <Sender-Email-ID>
msg['To'] = "" # <Reciever-Email-ID>

# sending the mail
for i in range(10000): # 10000 can be replaced by number of emails to be sent.
	s.send_message(msg)

# terminating the session
s.quit()
