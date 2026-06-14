# Programación tradicional
def registrar_mascota():
    print("=== Registro de mascotas ===")

    nombre = input("Ingrese nombre de la mascota: ")
    especie = input("Ingrese especie de la mascota: ")
    edad = input("Ingrese edad de la mascota: ")

    return nombre, especie, edad


def mostrar_mascota(nombre, especie, edad):
    print("\n=== Información Registrada ===")
    print(f"Nombre   : {nombre}")
    print(f"Especie  : {especie}")
    print(f"Edad     : {edad} años")


# Programa principal
nombre, especie, edad = registrar_mascota()
mostrar_mascota(nombre, especie, edad)