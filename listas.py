#       POSICIÓN
#           2nd
#        1er   3er  4º
lista = [3, 7, 5.0, "patata"]
#        0  1    2   3
#        Índice

print(lista, type(lista))

# se ve el 5.0
print(lista[2])

# 3 + 1 = 4
print(lista[0] + 1)

# Modificamos elementos en la lista
lista[1] = 99
print(lista)

# Propiedad longitud
longitud = len(lista)
print(f"La lista contiene {longitud} elementos")
print(longitud, type(longitud))


if "patata" in lista:
    print("La lista es digna del reino Patata")
else:
    print("Esta lista no vale")

lista.append("Naranja")
lista.append(1000)

print(lista)


lista.remove(5.0)
lista.pop(0)
print(lista)


lista_corta = ["a", "b", "c"]


lista.append(lista_corta)
lista.append([1, [4, 5, [7, 8, 9]], 3])
print(lista)
print(" -" * 30)
print(lista[4][0])
print(lista[5][1])
print(lista[5][1][2][1])  # EL OCHO


# Accedemos aposiciones de un string
print(lista[2][0])
print(lista[2][5])

# variable = lista[2][5]
# funcion(lista[2][5])

for x in lista:
    print("    · ", x)


indice = 0
while indice < len(lista):
    dato = lista[indice]
    indice += 1
    print("    · ", dato)
