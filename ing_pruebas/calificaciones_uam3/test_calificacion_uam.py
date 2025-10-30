import unittest
from calificacion import calificacion_uam   # asumiendo que guardaste la función en calificacion.py

class TestCalificacionUAM(unittest.TestCase):

    # def test_calificacion_a(self):
    #     """Test para la calificación 'A'"""
    #     for i in range(88,101):
    #         puntaje=i/10
    #         #with self.subTest(puntaje=puntaje):
    #         self.assertEqual(calificacion_uam(puntaje), "A")

    # def test_calificacion_b(self):
    #     """Test para la calificación 'B'"""
    #     self.assertEqual(calificacion_uam(7.5), "B")
    #     self.assertEqual(calificacion_uam(8.9), "B")

    # def test_calificacion_c(self):
    #     """Test para la calificación 'S'"""
    #     self.assertEqual(calificacion_uam(6), "S")
    #     self.assertEqual(calificacion_uam(7.4), "S")
        
    # def test_calificacion_c(self):
    #     """Test para la calificación 'NA'"""
    #     self.assertEqual(calificacion_uam(5.9), "NA")
    #     self.assertEqual(calificacion_uam(0), "NA")

    # def test_puntaje_invalido_negativo(self):
    #     """Test para puntaje inválido negativo"""
    #     self.assertEqual(calificacion_uam(-1), "Puntaje inválido: -1")

    # def test_puntaje_invalido_mayor(self):
    #     """Test para puntaje inválido mayor que 10"""
    #     self.assertEqual(calificacion_uam(11), "Puntaje inválido: 11")

    # Pruebas para excepciones
    def test_puntaje_fuera_de_rango(self):
        """Debe lanzar ValueError si el puntaje está fuera del rango 0–10"""
        with self.assertRaisesRegex(ValueError, r"^El puntaje debe estar entre 0 y 10"):
            calificacion_uam(-1)

        with self.assertRaisesRegex(ValueError, r"^El puntaje debe estar entre 0 y 10"):
            calificacion_uam(11)

    def test_tipo_incorrecto(self):
        """Debe lanzar TypeError si el tipo de dato no es numérico"""
        with self.assertRaisesRegex(TypeError, r"^El puntaje debe ser numérico"):
            calificacion_uam("9")

        with self.assertRaisesRegex(TypeError, r"^El puntaje debe ser numérico"):
            calificacion_uam(None)



if __name__ == "__main__":
    unittest.main(verbosity=2)

# Aun por verse estudiar jeje 