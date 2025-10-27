# test_cuenta.py
import unittest
from cuenta import CuentaBancaria

class TestCuentaBancaria(unittest.TestCase):

    def test_instancia(self):
            """Crear una CuentaBancaria y verificar su tipo."""
            cuenta_bancaria = CuentaBancaria("Samuel", 1000)

            # Es instancia de CuentaBancaria
            self.assertIsInstance(cuenta_bancaria, CuentaBancaria)

            # No es instancia de dict
            self.assertNotIsInstance(cuenta_bancaria, dict)

    def test_depositar_retirar(self):
        """Probar depositar (varios montos) y retirar (válido e inválidos)."""
        
        # 1️Crear cuenta y saldo inicial
        cuenta = CuentaBancaria("Saul", 0)
        saldo_esperado = 0

        # 2️ Depósitos con varios montos (aquí sí usamos subTest dentro del for)
        for monto in [100, 50, 25]:
            with self.subTest(deposito=monto):
                saldo_esperado += monto
                self.assertEqual(cuenta.depositar(monto), saldo_esperado)

        # 3️ Retiro válido (sin with)
        saldo_esperado -= 50
        self.assertEqual(cuenta.retirar(50), saldo_esperado)

        # 4️Retiro inválido (mayor al saldo)
        self.assertEqual(cuenta.retirar(9999), "Saldo insuficiente")
        self.assertEqual(cuenta.obtener_saldo(), saldo_esperado)

        # 5️Retiro con monto no válido (<= 0)
        self.assertEqual(cuenta.retirar(0), "Monto inválido")
        self.assertEqual(cuenta.obtener_saldo(), saldo_esperado)


    def test_transferencias(self):
            """Transferencia válida/ inválida y verificación de saldos."""
            cuenta1 = CuentaBancaria("A", 300)
            cuenta2 = CuentaBancaria("B", 100)

            # Transferencia válida 200 de cta1 a cta2
            self.assertTrue(cuenta1.transferir(200, cuenta2))
            self.assertEqual(cuenta1.obtener_saldo(), 100)
            self.assertEqual(cuenta2.obtener_saldo(), 300)

            # Transferencia inválida (monto > saldo disponible)
            self.assertFalse(cuenta1.transferir(500, cuenta2))
            self.assertEqual(cuenta1.obtener_saldo(), 100)
            self.assertEqual(cuenta2.obtener_saldo(), 300)

    def test_saldo_final(self):
            """Comprobar saldo final correcto e incorrecto con asserts booleanos."""
            cuenta = CuentaBancaria("C", 50)
            cuenta.depositar(150)   # -> 200
            cuenta.retirar(40)      # -> 160

            saldo = cuenta.obtener_saldo()
            self.assertTrue(saldo == 160)    # saldo correcto
            self.assertFalse(saldo == 9999)  # saldo incorrecto

   

if __name__ == "__main__":
    unittest.main(verbosity=2)
