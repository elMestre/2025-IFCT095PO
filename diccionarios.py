lista = [3, 7, 5.0, "patata"]

# print(lista[10])

diccionario = {
    "peso": 3,
    "luces": 7,
    "version": 5.0,
    "codename": "paTata",
    "lista": lista,
    "dicc": {
        "a": 1,
        "b": 2
    }
}

coches = [{
    "nombre": "citroen",
    "precio": 1000,
    "potencia": 100
}, {
    "nombre": "bmw",
    "precio": 3000,
    "potencia": 180
}]


for coche in coches:
    print(coche["nombre"], ": ", coche["potencia"] * coche["precio"] )


print(diccionario["luces"])
print(diccionario["codename"][2])
print(diccionario["dicc"]["a"])

# print(diccionario["avion"])

print(diccionario)


# JSON

import json

# a Python object (dict):
x = {
  "name": "John",
  "age": 30,
  "city": "New York"
}

# convert into JSON:
y = json.dumps(x)

# the result is a JSON string:
print("TYPE: ", type(x), "LEN:", len(x)) 
print("TYPE: ", type(y), "LEN:", len(y)) 
print(y)


# EJERCICIO
"""
El programa solicitará datos al usuario uno detrá de otro
crearemos una lista de coches iguales
al final mostramos la lista
"""

def introducir_vehiculo(id: int):
    vehiculo = {'id': id}

    for dato in  ["marca", "precio", "potencia", "color"]:
        vehiculo[dato] = input(f"{dato}:")

    return vehiculo

def validar_vehiculo(vehiculo):
    for llave in vehiculo:
        if vehiculo[llave] == '':
            return False

    return True

def introducir_vehiculos():
    vehiculos = []
    while True:
        print()
        v = introducir_vehiculo(len(vehiculos))
        if validar_vehiculo(v):
            vehiculos.append(v)
        else:
            break

    return vehiculos

def mostrar(vehiculo):
    print(f"==[{vehiculo["id"]}]")
    for llave in vehiculo:
        if llave != "id":
            print(f"{llave}: {vehiculo[llave]}")
    print("-" * 5)

for vehiculo in introducir_vehiculos():
    mostrar(vehiculo)

