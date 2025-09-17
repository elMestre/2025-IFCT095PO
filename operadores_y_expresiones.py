a = 1
b = 2
c = 3
# d = (a + b) * (ju + je + (hu + he) + jo)
# print(d)

'''
# Operador de asignación
=

# Operador de igualdad
==
'''

# Cuando defino una funcion, este codigo NO se jecuta


def hipotenusa(a, b):
    h = (a**2 + b**2)**(1/2)
    print("HIPOTENUSA DE ", a, " ", b)

    return h

# El código se ejuca cada vez que se invoca (llama) la función
algo = hipotenusa(1, 1)
algo = hipotenusa(1, 2)
algo = hipotenusa(1, 3)
algo = hipotenusa(2, 2)
print(algo)
algo = hipotenusa(2, 3)
