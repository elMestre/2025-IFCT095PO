# Punto 1: Las funciones son un dato como cualquier otro

from time import sleep


def diga_el_numero(x):
    print(f"EL NUM ES: {x}")


def procesa_datos(funcion_callback):

    contador = 0
    for i in range(10):
        contador += i
        print("- ", i)
        sleep(0.2)

    funcion_callback(contador)


print(type(1))
print(type(1.0))
print(type("1"))
print(type(diga_el_numero))

# procesa_datos(diga_el_numero)
