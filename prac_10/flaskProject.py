from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return "<h1>Hello World :)</h1>"


@app.route('/greet')
@app.route('/greet/<name>')
def greet(name=""):
    return f"Hello {name}"


@app.route('/f/<celsius>')
def calculate_fahrenheit_from_celsius(celsius):
    """Calculate fahrenheit from celsius."""
    fahrenheit = float(celsius) * 9.0 / 5 + 32
    return f"Input Celsius: {celsius} - Converted Fahrenheit: {fahrenheit:.2f}"


@app.route('/c/<fahrenheit>')
def calculate_celsius_from_fahrenheit(fahrenheit):
    """Calculate celsius from fahrenheit."""
    celsius = 5 / 9 * (float(fahrenheit) - 32)
    return f"Input Fahrenheit: {fahrenheit} - Converted Celsius: {celsius:.2f}"


if __name__ == '__main__':
    app.run()
