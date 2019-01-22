import sys
import smtplib
from email.message import EmailMessage

with open(r"C:\Users\ilu25\PycharmProjects\helloPython\test.txt") as fb :
    msg = EmailMessage
    msg.set_content(fb.read())
msg['Subject'] = "The contest of %s" % r"C:\Users\ilu25\PycharmProjects\helloPython\test.txt"
msg["From"] = "1634295715@qq.om"
msg["To"] = "hhdxpg@gmail.com"

s = smtplib.SMTP("localhost")
s.send_message(msg)
s.quit()
