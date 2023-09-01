from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello, Bitch!"

@app.route('/apple')
def page():
    return "Hello, 사과!"
if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=80)