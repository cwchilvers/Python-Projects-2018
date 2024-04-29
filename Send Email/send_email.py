import smtplib

# create subject (modules)
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

from email.mime.base import MIMEBase

# import encoders

from email import encoders

# define variables
email_user = 'email@email.com'
email_rec = 'email@email.com'
pw = 'password'

#define subject
subject = 'Python!'

msg = MIMEMultipart()
msg['From'] = email_user
msg['To'] = email_rec
msg['Subject'] = subject

body = 'Hello. Sending this email from Python!'
msg.attach(MIMEText(body, 'plain')) # attach msg to body

# attachment
filename = 'ipconfig.py'
attachment = open((filename), 'rb') # open file and read it

part = MIMEBase('application', 'octet-stream') # basically uploading attachment and closing it
part.set_payload((attachment).read()) # read attachment and set as payload
encoders.encode_base64(part) # standard encoding for emails (text and images, too)
part.add_header('Content-Disposition', "attachment; filename= "+filename)

msg.attach(part) # attach previous thing to rest of message

text = msg.as_string() # convert message to a plain-text string
server = smtplib.SMTP('smtp.gmail.com',587) # server and port num
server.starttls() # initializes secure connection
server.login(email_user, pw)


server.sendmail(email_user, email_rec, text) # (sender's address, reciever's address)
server.quit()
