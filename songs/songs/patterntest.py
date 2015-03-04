__author__ = 'Omkareshwar'

from pattern.web import Twitter, plaintext, Wikipedia, URL, PDF
import smtplib

d = ''
twitter = Twitter(language='en')
for tweet in twitter.search('"#CWC15"', cached=False):
    print plaintext(tweet.text)
    d = d + plaintext(tweet.text)


sender = 'alpha@nikitph.com'
receivers = 'nikitph@gmail.com'

message = """From: alpha <alpha@nikitph.com>
To: To Person <nikitph@gmail.com>
Subject: SMTP e-mail test

This is a test e-mail message.
"""

try:
   smtpObj = smtplib.SMTP('mail.nikitph.com', 26)
   smtpObj.login(sender,'')
   print "login"
   smtpObj.sendmail(sender, receivers, message)
   print "Successfully sent email"
except:
    "error"