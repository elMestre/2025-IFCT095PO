# Parámetros por defecto:
# Si no se indica el IVA sera el 21%
def calculo(importe: int, iva: float) -> float:

    if type(importe) is not int:
        print("importe debe ser un int")

    return None

    importe += importe * iva

    return importe


print(calculo(100, 0))
print(calculo(100.0, 0.16))
print(calculo("patata", 3))
