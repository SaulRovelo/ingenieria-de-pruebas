# test_cuenta.py
import sys
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

    @unittest.skip("Versión previa: esperaba 'Monto inválido'; ahora se usan excepciones")
    def test_depositar_retirar(self):
        """Probar depositar (varios montos) y retirar (válido e inválidos)."""
        # 1) Crear cuenta y saldo inicial
        cuenta = CuentaBancaria("Saul", 0)
        saldo_esperado = 0

        # 2) Depósitos con varios montos (usando subTest en el for)
        for monto in [100, 50, 25]:
            with self.subTest(deposito=monto):
                saldo_esperado += monto
                self.assertEqual(cuenta.depositar(monto), saldo_esperado)

        # 3) Retiro válido
        saldo_esperado -= 50
        self.assertEqual(cuenta.retirar(50), saldo_esperado)

        # 4) Retiro inválido (mayor al saldo)
        self.assertEqual(cuenta.retirar(9999), "Saldo insuficiente")
        self.assertEqual(cuenta.obtener_saldo(), saldo_esperado)

        # 5) Retiro con monto no válido (<= 0)
        self.assertEqual(cuenta.retirar(0), "Monto inválido")
        self.assertEqual(cuenta.obtener_saldo(), saldo_esperado)

    # 2) SkipIf — solo se omite en Windows (por ejemplo)
    @unittest.skipIf(sys.platform == "win32", "No se ejecuta en Windows")
    def test_transferencias(self):
        """Transferencia válida/ inválida y verificación de saldos."""
        cuenta1 = CuentaBancaria("A", 300)
        cuenta2 = CuentaBancaria("B", 100)

        # Transferencia válida: 200 de cta1 a cta2
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

    # -------------------------------------------

    # --- NUEVAS PRUEBAS: EXCEPCIONES POR TIPO (TypeError) ---
    # 3) SkipUnless — solo se ejecuta en Windows
    @unittest.skipUnless(sys.platform == "win32", "Solo se ejecuta en Windows")
    def test_excepcion_tipo_invalido_en_todas(self):
        """TypeError cuando el monto NO es numérico (depositar/retirar/transferir)."""
        c1 = CuentaBancaria("A", 100)
        c2 = CuentaBancaria("B", 50)
        invalidos = [None, "100", [], {}, 5 + 2j]  # None, cadena, lista, dict, complejo

        for valor in invalidos:
            with self.subTest(metodo="depositar", monto=valor):
                with self.assertRaises(TypeError):
                    c1.depositar(valor)

            with self.subTest(metodo="retirar", monto=valor):
                with self.assertRaises(TypeError):
                    c1.retirar(valor)

            with self.subTest(metodo="transferir", monto=valor):
                with self.assertRaises(TypeError):
                    c1.transferir(valor, c2)

    # --- NUEVAS PRUEBAS: EXCEPCIONES POR VALOR (ValueError) ---
    def test_excepcion_valor_invalido_en_todas(self):
        """ValueError cuando el monto <= 0 (depositar/retirar/transferir)."""
        c1 = CuentaBancaria("A", 100)
        c2 = CuentaBancaria("B", 50)

        for monto in [-100, -1, 0]:
            with self.subTest(metodo="depositar", monto=monto):
                with self.assertRaises(ValueError):
                    c1.depositar(monto)

            with self.subTest(metodo="retirar", monto=monto):
                with self.assertRaises(ValueError):
                    c1.retirar(monto)

            with self.subTest(metodo="transferir", monto=monto):
                with self.assertRaises(ValueError):
                    c1.transferir(monto, c2)

    # --- NUEVA VERSIÓN de depositar/retirar (ahora con excepciones y subTest) ---
    def test_depositar_retirar_excepciones(self):
        """Depositar/retirar válidos y errores por valor; usa subTest y respeta mensajes existentes."""
        cuenta = CuentaBancaria("Saul", 0)
        saldo_esperado = 0

        # Depósitos válidos
        for monto in [100, 50, 25]:
            with self.subTest(deposito=monto):
                saldo_esperado += monto
                self.assertEqual(cuenta.depositar(monto), saldo_esperado)

        # Retiro válido
        with self.subTest(retiro=50):
            saldo_esperado -= 50
            self.assertEqual(cuenta.retirar(50), saldo_esperado)

        # Retiro mayor al saldo (se mantiene comportamiento original)
        with self.subTest(retiro_mayor_al_saldo=9999):
            self.assertEqual(cuenta.retirar(9999), "Saldo insuficiente")
            self.assertEqual(cuenta.obtener_saldo(), saldo_esperado)

        # Retiros inválidos (<= 0) ahora deben lanzar ValueError
        for monto in [0, -1, -50]:
            with self.subTest(retiro_invalido=monto):
                with self.assertRaises(ValueError):
                    cuenta.retirar(monto)


if __name__ == "__main__":
    unittest.main(verbosity=2)
