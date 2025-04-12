def celsius_para_fahrenheit(celsius):
    return (celsius * 9/5) + 32


def fahrenheit_para_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9


def celsius_para_kelvin(celsius):
    return celsius + 273.15


def kelvin_para_celsius(kelvin):
    return kelvin - 273.15


def fahrenheit_para_kelvin(fahrenheit):
    celsius = fahrenheit_para_celsius(fahrenheit)
    return celsius_para_kelvin(celsius)


def kelvin_para_fahrenheit(kelvin):
    celsius = kelvin_para_celsius(kelvin)
    return celsius_para_fahrenheit(celsius)
