# Comparamos paso por referencia y copia

a1 = [1, 2, 3]
b1 = a1
b1[2] = 11
print("PASO POR REFERENCIA")
print("list a1:", a1)
print("list b1:", b1)
print("address of a1:", id(a1))
print("address of b1", id(b1))
print("--------------------")

print()
print("PASO POR COPIA")

import copy

a2 = [1, 2, 3]
b2 = copy.copy(a2)
b2[2] = 11
print("list a2:", a2)
print("list b2:", b2)
print("address of a2:", id(a2))
print("address of b2", id(b2))
