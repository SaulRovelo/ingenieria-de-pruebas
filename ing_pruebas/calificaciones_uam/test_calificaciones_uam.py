import unittest
from calificaciones_uam.calificaciones_uam import calificacion

class test_calificacion(unittest.TestCase):
    def test_calificacionA(self):
        self.assertEqual(calificacion(9.7), "A")
        self.assertEqual(calificacion(9.8), "A")
    
    def test_calificacionB(self):
        self.assertEqual(calificacion(8), "B")
        self.assertEqual(calificacion(8.1), "B")
    
    def test_calificacionS(self):
        self.assertEqual(calificacion(6.2), "S")
        
    def test_calificacionNA(self):
        self.assertEqual(calificacion(1), "NA")

#Ejecutar el codigo
if __name__ == "__main__":
    unittest.main(verbosity=1)