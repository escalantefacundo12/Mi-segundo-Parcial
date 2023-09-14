""" Escribe un programa que encuentre y
muestre todos los números primos dentro de un rango dado. Utiliza una función modular
para determinar si un número es primo. """

# Función para determinar si un número es primo
def es_primo(numero):
    if numero <= 1:
        return 0  # Los números menores o iguales a 1 no son primos
    if numero <= 3:
        return 1  # 2 y 3 son primos

    if numero % 2 == 0 or numero % 3 == 0:
        return 0

    i = 5
    while i * i <= numero:
        if numero % i == 0 or numero % (i + 2) == 0:
            return 0
        i += 6

    return 1

# Solicitamos al usuario que ingrese el rango
inicio = int(input("Ingrese el número de inicio del rango: "))
fin = int(input("Ingrese el número de fin del rango: "))

print("Números primos en el rango de", inicio, "a", fin, ":")

# Encontramos y mostramos los números primos en el rango dado
for numero in range(inicio, fin + 1):
    if es_primo(numero):
        print(numero)
