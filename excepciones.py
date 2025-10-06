def detalles(variable):
    print(variable, type(variable))


if __name__ == "__main__":
    entero = 3
    flotante = 3.0
    cadena = "3"

    detalles(entero)
    detalles(flotante)
    detalles(cadena)

    try:
        print(f"DIVISION POR CERO: {1 / 0}")
        print(entero + cadena)
    except TypeError:
        print("Falla por que no son de tipo compatible")
        # pedirle_al_usuario_nuevo_cadena()
    except ZeroDivisionError:
        print("WARN: Division por cero detectada")

    # ---------------------------

    try:
        print(f"DIVISION POR CERO: {1 / 0}")
    except ZeroDivisionError:
        print("WARN: Division por cero detectada")

    try:
        print(entero + cadena)
    except TypeError:
        print("Falla por que no son de tipo compatible")
        # pedirle_al_usuario_nuevo_cadena()
