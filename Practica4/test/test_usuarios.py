import unittest
from Practica4.src.biblioteca import Libro, Usuario

# usar src como carpeta base
#import sys
#import os
#sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))
#from biblioteca import Libro, Usuario

class TestUsuario(unittest.TestCase):
    """Pruebas unitarias para la clase Usuario"""

    def setUp(self):
        self.libro1 = Libro("1984", "George Orwell", 328)
        self.libro2 = Libro("Fahrenheit 451", "Ray Bradbury", 256)
        self.usuario = Usuario("Saul")

    def test_prestar_y_devolver_libro(self):
        """ Prueba préstamo y devolución de libros usando subTest"""
        for libro in [self.libro1, self.libro2]:
            with self.subTest(libro=libro): ## Con el with y subTest nos permite probar cada libro por separado, aunque uno falle el otro se prueba igual
                mensaje_prestamo = self.usuario.prestar_libro(libro) #Prestamos el libro
                self.assertIn(libro, self.usuario.libros_prestados) #Verificamos que el libro esté en la lista de prestados
                self.assertEqual(mensaje_prestamo, f"{libro.titulo} prestado a {self.usuario.nombre}") #Verificamos el mensaje de préstamo
                

                mensaje_devolucion = self.usuario.devolver_libro(libro) #Devolvemos el libro
                self.assertNotIn(libro, self.usuario.libros_prestados) #Verificamos que el libro ya no esté en la lista de prestados
                self.assertEqual(mensaje_devolucion, f"{libro.titulo} devuelto por {self.usuario.nombre}") #Verificamos el mensaje de devolución

    def test_devolver_sin_prestar(self):
        """ Verifica que no se pueda devolver un libro no prestado"""
        with self.assertRaisesRegex(ValueError, r"^Saul no tiene prestado"):
            self.usuario.devolver_libro(self.libro1)

    def test_prestar_objeto_incorrecto(self):
        """ Verifica que solo se puedan prestar objetos de tipo Libro"""
        with self.assertRaisesRegex(TypeError, r"^Solo se puede prestar un objeto Libro"):
            self.usuario.prestar_libro("no es un libro")


#Setup: se ejecuta antes de cada prueba, para preparar el entorno de prueba
#en este caso prepara tres objetos validos