import unittest
from Practica4.src.biblioteca import Libro

# usar src como carpeta base para importar módulos
#import sys
#import os
#sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))
#from biblioteca import Libro

class TestLibro(unittest.TestCase):
    """Pruebas unitarias para la clase Libro"""

    def test_creacion_libro_valido(self):
        """Verifica la creación correcta de un libro válido"""
        libro = Libro("Cien años de soledad", "Gabriel García Márquez", 471)
        self.assertEqual(libro.titulo, "Cien años de soledad")
        self.assertEqual(libro.autor, "Gabriel García Márquez")
        self.assertEqual(libro.paginas, 471)

    def test_creacion_libro_paginas_invalidas(self):
        """Verifica que falle si el número de páginas es inválido"""
        with self.assertRaisesRegex(ValueError, r"^El número de páginas debe ser un entero positivo"):
            Libro("El Quijote", "Cervantes", -10)

    def test_creacion_libro_autor_titulo_invalido(self):
        """Verifica que falle si título o autor no son cadenas"""
        with self.assertRaisesRegex(TypeError, r"^Título y autor deben ser strings"):
            Libro(123, 20, 200)
