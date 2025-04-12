import unittest
from src.conversor_temperatura import (
    celsius_para_fahrenheit, fahrenheit_para_celsius,
    celsius_para_kelvin, kelvin_para_celsius,
    fahrenheit_para_kelvin, kelvin_para_fahrenheit
)


class TestConversorTemperatura(unittest.TestCase):

    # Teste se a conversão de Celsius para Fahrenheit está correta
    def test_celsius_para_fahrenheit(self):
        self.assertEqual(celsius_para_fahrenheit(0), 32)
        self.assertEqual(celsius_para_fahrenheit(100), 212)

    # Teste se a conversão de Fahrenheit para Celsius está correta
    def test_fahrenheit_para_celsius(self):
        self.assertEqual(fahrenheit_para_celsius(32), 0)
        self.assertEqual(fahrenheit_para_celsius(212), 100)

    # Teste se a conversão de Celsius para Kelvin está correta
    def test_celsius_para_kelvin(self):
        self.assertEqual(celsius_para_kelvin(0), 273.15)
        self.assertEqual(celsius_para_kelvin(100), 373.15)

    # Teste se a conversão de Kelvin para Celsius está correta
    def test_kelvin_para_celsius(self):
        self.assertEqual(kelvin_para_celsius(273.15), 0)
        self.assertEqual(kelvin_para_celsius(373.15), 100)

    # Teste se a conversão de Fahrenheit para Kelvin está correta
    def test_fahrenheit_para_kelvin(self):
        self.assertEqual(fahrenheit_para_kelvin(32), 273.15)
        self.assertEqual(fahrenheit_para_kelvin(212), 373.15)

    # Teste se a conversão de Kelvin para Fahrenheit está correta
    def test_kelvin_para_fahrenheit(self):
        self.assertEqual(kelvin_para_fahrenheit(273.15), 32)
        self.assertEqual(kelvin_para_fahrenheit(373.15), 212)


if __name__ == '__main__':
    unittest.main()
