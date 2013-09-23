import webapp2
import urllib
from google.appengine.api import mail
import sys

class MainPage(webapp2.RequestHandler):
  def get(self):
      self.response.headers['Content-Type'] = 'text/plain'
      self.response.write('Hello!')

class CheckServer(webapp2.RequestHandler):
  def sendmail(self, errormsg):

    sender_address = "Sender <sensder@mydomain.com>"
    user_address = "Admin <admin@mydomain.com>"
    subject = "Web Server Alarm!"
    body = errormsg

    self.response.write(body)

    mail.send_mail(sender_address, user_address, subject, body)
  def get(self):
      self.response.headers['Content-Type'] = 'text/plain'

      try:
        code = urllib.urlopen("http://mydomain.com").getcode()
        if(code!=200):
          self.sendmail('HTTP Code: '+str(code))
      except IOError as e:
        self.sendmail("I/O error({0}): {1}".format(e.errno, e.strerror))
      except Exception as x:
        self.sendmail(str(x))


application = webapp2.WSGIApplication([
  ('/check', CheckServer),
  ('/', MainPage),
  ], debug=True)