from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World from Chris Hauser! This is my code change.'

@app.route('/hello')
def hello():
    return render_template('hello.html')
@app.route('/about')
def about():
    return render_template('about.html')
if __name__ == '__main__':
    app.run()

@app.route('/about-css')
def about():
    return render_template('about-css.html')
if __name__ == '__main__':
    app.run()
