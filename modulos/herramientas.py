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


precalculado = {
    "fibonacci": [1, 1, 2, 3, 5, 8, 13],
    "exponencial": [1, 1, 2, 6, 25, 125, 725]
}


if __name__ == "__main__":
    print(f"Mi __name__ es: {__name__}")
    print("Prueba para pedir un entero")
    a = pedir_entero()

    if isinstance(a, int):
        print("si: INT")
    else:
        print("ERROR")
else:
    print(f"Importamos el modulo {__name__}")
