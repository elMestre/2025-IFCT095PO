# Definimos la clase

class ContenedorLiquido:
    _SORBO = 50  # CONSTANTE

    def beber(self):
        if self.cantidad >= ContenedorLiquido._SORBO:
            self.cantidad -= ContenedorLiquido._SORBO
            print(f"Has bebido del contendor {self}")
        else:
            print(f"NO QUEDA BASTANTE LíQUIDO en {self}")


class Taza(ContenedorLiquido):
    def __init__(self, color, cantidad):
        self.color = color
        self.cantidad = cantidad
        print(f"SE HA CREADO UNA taza {self.color}")

    def __str__(self):
        return f"TAZA {self.color} CANTIDAD {self.cantidad}ml"


class Copa(ContenedorLiquido):
    def __init__(self, cantidad):
        self.cantidad = cantidad
        print(f"SE HA CREADO UNA copa de {self.cantidad}ml")

    def __str__(self):
        return f"COPA CANTIDAD {self.cantidad}ml"


recipientes = [
    Taza("rojo", 300),
    Taza("azul", 250),
    Taza("verde", 500),
    Copa(100),
    Taza("verde", 200),
    Copa(300)
]

print()
print("############################################")
print()

for recipiente in recipientes:
    print(type(recipiente))
    print(recipiente)
    recipiente.beber()
    print(recipiente)
    print("---")
    print()
