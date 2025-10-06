# Ejercicios

## 1

- suma el precio de dos articulos (precio fijo)
- aplica el IVA
- muestra el PVP al usuario


## 2

- Modifica el ejercicio anterior:
    - Si el resultado es inferior a un TOTAL (ej 15)
        - saldra el mensaje de "Puedes comprarlo"
    - En caso contrario el mesaje rezará:
        - "No hay suficientes fondos"

## 3 e.control

- Escribe código que haga la cuenta atrás de un cohete

ej:

```
10
9
8
7
6
5
4
3
2
1
DESPEGUE!
BROOOOOOOMMMMMM
---------------
```

- Vamos a comprobar si sale a cuenta despegar con un avión
    - Si hay pocos pasajeros (POCOS < 25) no vale pena despegar
    - Si hay demasiados pasajeros (MAX_AVION=150) ¿Vale la pena fletar un segundo avión?


## Funciones

Resuelve estos ejercicios usando funciones

- Crea un codigo en una funcion que devuela el cuadrado de un numero `num`
si `num` es negativo devuelve `None` en su lugar
- Muestra por pantalla el saludo `¡Hola amiga!` cada vez que se la invoque.
- Escribir una función a la que se le pase una cadena `<nombre>` y muestre por pantalla el saludo `¡hola <nombre>!.`
- Escribir una función que calcule el total de una factura tras aplicarle el IVA. La función debe recibir la cantidad sin IVA y el porcentaje de IVA a aplicar, y devolver el total de la factura. Si se invoca la función sin pasarle el porcentaje de IVA, deberá aplicar un 21%.

- Escribir una función que reciba un número entero positivo y devuelva su factorial.

```
ej de factorial:
    4! => 4·3!
    3! => 3·2!
    4! => 4·3·2·1
    4! => 24
```

```python
def factorial(numero):
    pass

numero = 4
resultado = factorial(numero)
print("El factioral de {numero} es {resultado}")
```

## Casting, excepciones y recursividad

Crea una función recursiva Esta le pedria de al usuario un numero entero y seguirá pidiendoselo hasta que se introduzca un numero válido

Al final la funcion debe retornar el numero entero

## Listas

- Para cada palabra de una frase la imprimimos en una linea nueva

- Crea una lista e inicializala con 5 cadenas de caracteres leídas por teclado. Copia los elementos de la lista en otra lista pero en orden inverso, y muestra sus elementos por la pantalla.

- Explica el funcionamiento:

```python
print("Inicio de cuenta para el despegue...")
i = 60
while i > 0:
    i -= 1
    if i in [0, 10, 20, 30, 40, 50]:
        continue
        break
    print(f"T - {i}")

print("DESPEGUE...")

```
