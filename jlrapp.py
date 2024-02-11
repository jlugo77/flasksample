from flask import Flask, render_template

jlrapp = Flask(__name__)


@jlrapp.route('/')
def home():
    return render_template('home.html')


#if __name__ == "__main__":
#    jlrapp.run(host='0.0.0.0', port=80, debug=True)