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
