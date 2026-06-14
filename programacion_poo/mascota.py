class Mascota:
    def __init__(self, nombre, especie, edad):
        self.nombre = nombre
        self.especie = especie
        self.edad = edad

    def mostrar_informacion(self):
        print("=== Información de la Mascota ===")
        print(f"Nombre: {self.nombre}")
        print(f"Especie: {self.especie}")
        print(f"Edad: {self.edad} años")

    def hacer_sonido(self):
        if self.especie.lower() == "perro":
            print(f"{self.nombre} dice: ¡Guau guau!")
        elif self.especie.lower() == "gato":
            print(f"{self.nombre} dice: ¡Miau!")
        else:
            print(f"{self.nombre} hace un sonido característico de su especie.")


# Crear objetos
mascota1 = Mascota("Max", "Perro", 4)
mascota2 = Mascota("Luna", "Gato", 2)

# Mostrar información y sonidos
mascota1.mostrar_informacion()
mascota1.hacer_sonido()

print()

mascota2.mostrar_informacion()
mascota2.hacer_sonido()