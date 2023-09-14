""" Crea un programa que permita convertir
entre Celsius y Fahrenheit. Crea dos funciones modulares: una para convertir de Celsius a
Fahrenheit y otra para convertir de Fahrenheit a Celsius. """

# Función para poder convertir de Celsius a Fahrenheit
def celsius_a_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

# Función para poder convertir de Fahrenheit a Celsius
def fahrenheit_a_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5/9
    return celsius

# Solicitar al usuario que ingrese la temperatura y la unidad de medida
temperatura = float(input("Ingrese la temperatura: "))
unidad = input("Ingrese la unidad de medida (C/F): ")

# Realizamos la conversión de temperatura según la unidad de medida ingresada
if unidad == "C" or unidad == "c":
    fahrenheit = celsius_a_fahrenheit(temperatura)
    print(str(temperatura) + " grados Celsius son equivalentes a " + str(fahrenheit) + " grados Fahrenheit.")
elif unidad == "F" or unidad == "f":
    celsius = fahrenheit_a_celsius(temperatura)
    print(str(temperatura) + " grados Fahrenheit son equivalentes a " + str(celsius) + " grados Celsius.")
else:
    print("Unidad de medida no válida. Use 'C' para Celsius o 'F' para Fahrenheit.")

