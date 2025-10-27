import unittest
import sys
from mascotas import Mascota


class TestMascotas(unittest.TestCase):
    

    def test_instancias(self):
        """Prueba que una mascota sea instancias de su clase y que no sea instancias
        de una clase incorrecta."""
        #Creamos instancia tipo Mascota
        Mascota_prueba = Mascota("Luna", "gato", 3)
        #Comprobamos que la instancia es del tipo correcto
        self.assertIsInstance(Mascota_prueba, Mascota)
        #Comprobamos que la instancia no es de un tipo incorrecto
        self.assertNotIsInstance(Mascota_prueba, int)

    def test_tipo_invalido(self):
        """Prueba que se levante una excepcion si se coloca un nombre incorrecto a
           una mascota."""
        #Creamos una lista de nombres inválidos
        lista_nombres_invalidos = [123, 45.6, None, [], {}]
        #Recorremos la lista y comprobamos que se lanza TypeError
        for nombre_invalido in lista_nombres_invalidos:
            with self.subTest(nombre=nombre_invalido): 
                with self.assertRaises(TypeError): # usamos typeError para comprobar la excepción
                    Mascota(nombre_invalido, "perro", 2)
        

    def test_edad_invalida(self):
        """Prueba que se levante una excepcion si se coloca un numero invalido de
        edad."""
        #Creamos una lista de edades inválidas
        lista_edades_invalidas = ["tres", -1, 4.5, None, [], {}]
        #Recorremos la lista y comprobamos que se lanza ValueError
        for edad_invalida in lista_edades_invalidas:
            with self.subTest(edad=edad_invalida): 
                with self.assertRaises(ValueError): # Usamos valueError para comprobar la excepción
                    Mascota("Luna", "gato", edad_invalida)



    @unittest.skipUnless(sys.platform == "win32", "Se ejecuta solo en Windows")
    def test_registro_chip(self):
        """Prueba que se registre correctamente el codigo del chip de una mascota.
            Esta prueba solo se debe ejecutar en tu sistema operativo."""
        #Creamos instancia tipo Mascota
        mascota = Mascota("Luna", "gato", 3)
        #Registramos el microchip
        mascota.registrar_microchip("ABC")
        self.assertEqual(mascota.microchip, "ABC") # Usamos Equal para comparar si es el mismo valor

    
    @unittest.skipIf(sys.platform == "darwin", "Esta prueba no se ejecuta en macOS")
    def test_chip_duplicado(self):
        """Prueba que se levante una excepcion al intentar registrar por segunda
           ocasion un chip a una mascota. Esta prueba, se debe saltar en MacOS."""
        #Creamos instancia tipo Mascota
        mascota = Mascota("Luna", "gato", 3)
        #Registramos el microchip
        mascota.registrar_microchip("ABC")
        #Intentamos registrar otro chip y comprobamos que lanza ValueError
        with self.assertRaises(ValueError):
            mascota.registrar_microchip("DEF")

    

if __name__ == "__main__":
    unittest.main(verbosity=2)
