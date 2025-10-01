def calcular_total(factura, iva=0.21, bonificacion=0):
    resultado = factura * (1 + iva) - bonificacion

    return resultado


factura1 = 100
factura2 = 150


total1 = calcular_total(factura1, 0.1, 10)
total2 = calcular_total(factura2)

print(f"El total de {factura1} es {total1}")
print(f"El total de {factura2} es {total2}")
