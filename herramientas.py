def pedir_entero():
    numero = None
    primera = True

    while not (type(numero) is int):
        msg = "Introduce un número entero. Si el número no es correcto, tendras que introducirlo de nuevo: "
        if not primera:
            msg = "No es correcto, introduce un entero válido, por favor: "
        primera = False

        numero = input(msg)
        try:
            numero = int(numero)
        except ValueError:
            pass

    return numero


n = pedir_entero()
print(f"El número introducido es: {n}")
