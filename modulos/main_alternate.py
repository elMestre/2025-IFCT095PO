from herramientas import pedir_entero, precalculado
# from herramientas import *

print("Hola, este es mi fichero principal")

entero = 100

while entero >= len(precalculado["fibonacci"]) or entero < 0:
    entero = pedir_entero()

print('·' * entero)
print(precalculado["fibonacci"][entero])
