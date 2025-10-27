class Electrodomestico:
    """Clase base para todos los electrodomésticos"""
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
    
class Lavadora(Electrodomestico):
    """Lavadora con capacidad de carga"""
    def __init__(self, marca, modelo, capacidad_carga):
        super().__init__(marca, modelo)
        self.capacidad_carga = capacidad_carga # en kg

class Refrigerador(Electrodomestico):
    """Refrigerador con volumen"""
    def __init__(self, marca, modelo, volumen):
        super().__init__(marca, modelo)
        self.volumen = volumen # en litros

def fabrica_electrodomestico(cls, *args, **kwargs):
    """Crea una instancia de la clase especificada"""
    return cls(*args, **kwargs)
# Ejemplo de uso:
# *args - argumentos posicionales
# **kwargs - argumentos nombrados
lavadora = fabrica_electrodomestico(Lavadora, "LG", "TwinWash", 10)