from flask import Flask, request, jsonify
from src.conversor_temperatura import (
    celsius_para_fahrenheit, fahrenheit_para_celsius,
    celsius_para_kelvin, kelvin_para_celsius,
    fahrenheit_para_kelvin, kelvin_para_fahrenheit
)

app = Flask(__name__)


@app.route('/')
def home():
    return "Bem-vindo à API de Conversão de Temperatura!"


# Rota para converter Celsius para Fahrenheit
@app.route('/celsius-to-fahrenheit', methods=['GET'])
def celsius_to_fahrenheit_view():
    celsius = float(request.args.get('celsius'))
    fahrenheit = celsius_para_fahrenheit(celsius)
    return jsonify({'celsius': celsius, 'fahrenheit': fahrenheit})


# Rota para converter Fahrenheit para Celsius
@app.route('/fahrenheit-to-celsius', methods=['GET'])
def fahrenheit_to_celsius_view():
    fahrenheit = float(request.args.get('fahrenheit'))
    celsius = fahrenheit_para_celsius(fahrenheit)
    return jsonify({'fahrenheit': fahrenheit, 'celsius': celsius})


# Rota para converter Celsius para Kelvin
@app.route('/celsius-to-kelvin', methods=['GET'])
def celsius_to_kelvin_view():
    celsius = float(request.args.get('celsius'))
    kelvin = celsius_para_kelvin(celsius)
    return jsonify({'celsius': celsius, 'kelvin': kelvin})


# Rota para converter Kelvin para Celsius
@app.route('/kelvin-to-celsius', methods=['GET'])
def kelvin_to_celsius_view():
    kelvin = float(request.args.get('kelvin'))
    celsius = kelvin_para_celsius(kelvin)
    return jsonify({'kelvin': kelvin, 'celsius': celsius})


# Rota para converter Fahrenheit para Kelvin
@app.route('/fahrenheit-to-kelvin', methods=['GET'])
def fahrenheit_to_kelvin_view():
    fahrenheit = float(request.args.get('fahrenheit'))
    kelvin = fahrenheit_para_kelvin(fahrenheit)
    return jsonify({'fahrenheit': fahrenheit, 'kelvin': kelvin})


# Rota para converter Kelvin para Fahrenheit
@app.route('/kelvin-to-fahrenheit', methods=['GET'])
def kelvin_to_fahrenheit_view():
    kelvin = float(request.args.get('kelvin'))
    fahrenheit = kelvin_para_fahrenheit(kelvin)
    return jsonify({'kelvin': kelvin, 'fahrenheit': fahrenheit})


if __name__ == '__main__':
    app.run(debug=True)
