def detalles(variable):
    print(variable, type(variable))


if __name__ == "__main__":
    entero = 3
    flotante = 3.0
    cadena = "3"

    detalles(entero)
    detalles(flotante)
    detalles(cadena)

    # Falla por que no son de tipo compatible
    # print(entero + cadena)

    input()

    a = float(3)
    x = int(1)
    y = int(2.8)
    z = int("3")
    # F = int("3.2")
    w = int(float("3.2"))

    detalles(a)
    detalles(x)
    detalles(y)
    detalles(z)
