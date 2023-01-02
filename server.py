
# ------------------------------------------------
# Program by Mircea Bularga
#
#
# Version      Date           Info
# 1.0          02-01-2023     Initial Version
#
# ----------------------------------------------
from flask import Flask, render_template

application = Flask(__name__)

@application.route('/')
def index():
   return render_template("info.html")

@application.route('/contacts/')
def contacts():
   return render_template("contacts.html")

if __name__ == '__main__':
   application.debug = True
   application.run()
