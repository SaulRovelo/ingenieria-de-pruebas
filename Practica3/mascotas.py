class Mascota:
    def __init__(self, nombre, especie, edad):
        if not isinstance(nombre, str):
            raise TypeError("El nombre debe ser una cadena de texto")
        if not isinstance(especie, str):
            raise TypeError("La especie debe ser una cadena de texto")
        if not isinstance(edad, int) or edad < 0:
            raise ValueError("La edad debe ser un entero no negativo")
        self.nombre = nombre
        self.especie = especie
        self.edad = edad
        self.microchip = None
        self.adoptada = False

    def registrar_microchip(self, codigo):
        if not isinstance(codigo, str):
            raise TypeError("El código de microchip debe ser una cadena")
        if self.microchip is not None:
            raise ValueError("La mascota ya tiene un microchip registrado")
        self.microchip = codigo

    def cumplir_anios(self):
        self.edad += 1

    def adoptar(self):
        if self.adoptada:
            raise ValueError("La mascota ya fue adoptada")
        self.adoptada = True
