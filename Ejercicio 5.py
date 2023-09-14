""": Escribe un programa que realice una búsqueda de un número
dado, en un arreglo. Crea una función modular para llevar a cabo la búsqueda"""

# Función para realizar la búsqueda de un número en un arreglo
def buscar_numero(arreglo, numero):
    for i in range(len(arreglo)):
        if arreglo[i] == numero:
            return i  # Si se encontró el número, devuelve la posición
    return -1  # si el número no se encontró, devuelve -1

numeros = [10, 5, 20, 15, 30, 25]

# Solicitamos al usuario que ingrese el número a buscar
numero_buscado = int(input("Ingrese el número que desea buscar: "))

# Realizamos la búsqueda
posicion = buscar_numero(numeros, numero_buscado)

# Mostramos el resultado de la búsqueda
if posicion != -1:
    print("El número", numero_buscado, "se encuentra en la posición", posicion, "del arreglo.")
else:
    print("El número", numero_buscado, "no se encuentra en el arreglo.")
