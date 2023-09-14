"""Crea un programa que permita realizar operaciones matemáticas
básicas (suma, resta, multiplicación y división) utilizando funciones modulares para cada
operación."""

# Función para realizar una suma
def suma(a, b):
    resultado = a + b
    return resultado

# Función para realizar una resta
def resta(a, b):
    resultado = a - b
    return resultado

# Función para realizar una multiplicación
def multiplicacion(a, b):
    resultado = a * b
    return resultado

# Función para realizar una división
def division(a, b):
    if b == 0:
        return "No es posible dividir por cero."
    resultado = a / b
    return resultado

# Solicitamos al usuario que ingrese dos números
num1 = float(input("Ingrese el primer número: "))
num2 = float(input("Ingrese el segundo número: "))

# Mostramos las operaciones disponibles y realizamos la operación seleccionada
print("Operaciones disponibles:")
print("1. Suma")
print("2. Resta")
print("3. Multiplicación")
print("4. División")

operacion = input("Seleccione una operación (1/2/3/4): ")

if operacion == "1":
    resultado = suma(num1, num2)
    print("El resultado de la suma es:", resultado)
elif operacion == "2":
    resultado = resta(num1, num2)
    print("El resultado de la resta es:", resultado)
elif operacion == "3":
    resultado = multiplicacion(num1, num2)
    print("El resultado de la multiplicación es:", resultado)
elif operacion == "4":
    resultado = division(num1, num2)
    print("El resultado de la división es:", resultado)
else:
    print("Operación no válida. Por favor, seleccione 1, 2, 3 o 4.")
