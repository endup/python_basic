import smtplib
from email.mime.text import MIMEText
from email.header import Header
import time
#以前还能用，现在好像多了挺多障碍
sender="W1601050172@163.com"
receiver="W1601050172@163.com"
subject="this is an email"
smtpserver="smtp.gmail.com"
username="W1601050172@163.com"
password="XXX"
mail_server_port=587

text="hello\n"
msg=MIMEText(text,'plain','utf-8')
msg['Subject']=Header(subject,'utf-8')

smtp=smtplib.SMTP(smtpserver,mail_server_port)
smtp.echo()
smtp.starttls()
smtp.login(username,password)
smtp.sendmail(sender,receiver,msg.as_string())
smtp.quit()
