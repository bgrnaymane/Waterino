from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('home.html')

@app.route('/aboutus')
def aboutus():
    return render_template('about_us.html')

@app.route('/signup')
def signup():
    return render_template('signup.html')


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8000, debug=True)
 