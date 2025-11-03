import unittest
from Practica4.test.test_libros import TestLibro
from Practica4.test.test_usuarios import TestUsuario


def suite_completa():
    pruebas = [
        unittest.defaultTestLoader.loadTestsFromTestCase(TestLibro),
        unittest.defaultTestLoader.loadTestsFromTestCase(TestUsuario)
    ]
    return unittest.TestSuite(pruebas)

if __name__ == "__main__":
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite_completa())


# Cuando uso: python -m Practica4.suite_biblioteca
#Lo que estamos haciendo es ejecutar una batería de pruebas personalizada (test suite),
#donde yo mismo selecciono qué clases de prueba incluir y en qué orden correrlas

# Cuando uso: python -m unittest discover -s test -p "test_*.py" -v
#Estoy usando el modo de descubrimiento automático. Python busca todos 
#los archivos de prueba que empiecen con test_ dentro de la carpeta test/ y los ejecuta
#y no tengo que crear un archivo especial de suite, todo se corre de forma automática.