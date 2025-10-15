# Ejemplo mental: ejecutamos código antes y/o despeus de la funcion decorada
def decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")
    return wrapper


def say_whee():
    print("Whee!")


say_whee = decorator(say_whee)
say_whee()


# ----------------------------------------------------------------------------------------------------
# Ejemplo sintáctico: ejecutamos el código de la funcion dos veces
def do_twice(func):
    def wrapper_do_twice(*args, **kwargs):
        func(*args, **kwargs)
        return func(*args, **kwargs)

    return wrapper_do_twice


# Ejemplo sintáctico: imprime informacion de la función
def function_info(func):
    def wrapper_function_info(*args, **kwargs):
        print(f"EJECUTAMOS una funcion con args: {len(args)} y kwargs: {len(kwargs)}")
        resultado = func(*args, **kwargs)
        print(f"El resultado es de tipo: {type(resultado)}")
        print()

        return resultado

    return wrapper_function_info


@do_twice
@function_info
def mi_funcion(msg1, msg2, msg3):
    print(f">>{msg1, msg2, msg3}<<")


mi_funcion("patata", "melón", "avión")


@function_info
def suma(a, b):
    resultado = a + b
    print(f"LA SUMA ES {resultado}")
    return resultado


print("TOTAL: ", suma(2, 3))
