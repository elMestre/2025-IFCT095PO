sumando_a = 3
sumando_b = 7
iva = 0.21    # IVA 21%

# opcion 1
suma = sumando_a + sumando_b
iva_calculado = suma * iva
pvp = suma + iva_calculado
print(pvp)

# opcion 2
print(sumando_a + sumando_b + (sumando_a + sumando_b) * iva)

# opcion 3
suma = sumando_a + sumando_b
print(suma + suma * iva)

# opcion 4
iva = 1.21 # IVA = 121% ?? =>> 100% + 21%
pvp = (sumando_a + sumando_b) * iva
print(pvp)
