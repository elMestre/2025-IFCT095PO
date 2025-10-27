# Definimos la clase
class Taza:
    # Atributo de clase:
    #    Compartido por todos los objetos
    cantidad_de_tazas = 0

    # Método: es una funcion asociada a un objeto
    def beber(self):
        print(f"Has bebido de la taza {self.color}")

    # En el método init inicializamos los
    #     atributos de instancia obligatorios
    def __init__(self, color):
        Taza.cantidad_de_tazas += 1
        self.color = color
        print(f"SE HA CREADO UNA taza {self.color}")

    def __str__(self):
        return f"TAZA {self.color}"


# Instanciamos objetos de la clase Taza
tazas = [
    Taza("rojo"),
    Taza("azul"),
    Taza("verde"),
    Taza("verde"),
    Taza("verde"),
    Taza("verde")
]

print()
print("############################################")
print()

for taza in [tazas[0]]:
    print(type(taza))
    print(taza)
    print("El color de la taza (a) es", taza.color)
    taza.beber()
    print(taza.cantidad_de_tazas)
    print("---")
    print()
