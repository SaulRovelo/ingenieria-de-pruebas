# electrodomesticos.py

class Electrodomestico:
    """Clase base para todos los electrodomésticos"""
    def __init__(self, marca, modelo):
        if not isinstance(marca, str) or not isinstance(modelo, str):
            raise TypeError("Marca y modelo deben ser strings")
        self.marca = marca
        self.modelo = modelo


class Lavadora(Electrodomestico):
    """Lavadora con capacidad de carga"""
    def __init__(self, marca, modelo, capacidad_carga):
        super().__init__(marca, modelo)
        if not isinstance(capacidad_carga, int):
            raise TypeError("La capacidad de carga debe ser un entero positivo")
        if capacidad_carga <= 0:
            raise ValueError("La capacidad de carga debe ser un entero positivo")
        self.capacidad_carga = capacidad_carga  # en kg


class Refrigerador(Electrodomestico):
    """Refrigerador con volumen"""
    def __init__(self, marca, modelo, volumen):
        super().__init__(marca, modelo)
        if not isinstance(volumen, int):
            raise TypeError("El volumen debe ser un entero positivo")
        if volumen <= 0:
            raise ValueError("El volumen debe ser un entero positivo")
        self.volumen = volumen  # en litros


def fabrica_electrodomestico(cls, *args, **kwargs):
    """Crea una instancia de la clase especificada"""
    return cls(*args, **kwargs)
