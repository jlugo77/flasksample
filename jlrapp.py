from flask import Flask, render_template

application = Flask(__name__)


@application.route('/')
def home():
    return render_template('home.html')


#if __name__ == "__main__":
#    application.run(host='0.0.0.0', port=80, debug=True)
    