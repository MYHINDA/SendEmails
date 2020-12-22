
import smtplib
from info import email_password,to,usr_name

server = smtplib.SMTP('smtp.gmail.com:587')
server.ehlo()
server.starttls()

fromaddr = ''
toaddrs  = to
username = usr_name
password = email_password



msg = "\r\n".join([
  "From: {}".format(fromaddr),
  "To: {}".format(toaddrs),
  "Subject: enter your subject here",
  "",
  "  enter your msg here"
  ]).encode('utf-8')

server.login(username, password)
server.sendmail(fromaddr, toaddrs, msg)