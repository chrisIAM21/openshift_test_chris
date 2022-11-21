from flask import Flask
import datetime

application = Flask(__name__)

@application.route("/")
#Retorna el dia de la semana
def hello():
    return datetime.datetime.now().strftime("%A")

if __name__ == "__main__":
    application.run()