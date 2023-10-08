from flask import Flask

web = Flask(__name__)

@web.route('/')
def hello_LegalEase():
  return render_template('home.html',company_name='LegalEase')

if __name__ == "__main__":
  web.run(host="0.0.0.0", debug=True)
