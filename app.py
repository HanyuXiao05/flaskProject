from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return '<h1>Hello World :)</h1>'


@app.route('/greet')
@app.route('/greet/<name>')
def greet(name=""):
    return f"Hello {name}"


@app.route('/f/<celsius>')
def f(celsius=0):
    return convert_temperature(celsius)


def convert_temperature(celsius):
    celsius = float(celsius)
    fahrenheit = celsius * 9.0 / 5 + 32
    return f"{fahrenheit:.2f}"


if __name__ == '__main__':
    app.run()
