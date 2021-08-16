import smtplib
import auth

gmail_user = 'adam2.siwiec@gmail.com'

sent_from = gmail_user
to = 'adam2.siwiec@gmail.com'
subject = 'Lorem ipsum dolor sit amet'
body = 'consectetur adipiscing elit'

try:
    smtp_server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    smtp_server.ehlo()
    smtp_server.login(gmail_user, auth.PASS)
    smtp_server.sendmail(sent_from, to, 'hi')
    smtp_server.close()
    print ("Email sent successfully!")
except Exception as ex:
    print ("Something went wrong….",ex)