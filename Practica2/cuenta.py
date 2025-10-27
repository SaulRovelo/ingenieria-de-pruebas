# cuenta.py
class CuentaBancaria:
    def __init__(self, titular, saldo=0):
        self.titular = titular
        self.saldo = saldo

    # Nuevo 
    def _validar_monto(self, monto):
        # Tipo
        if not isinstance(monto, (int, float)):
            raise TypeError(f"El monto debe ser numérico (int/float), se recibió {type(monto).__name__}")
        # Valor
        if monto <= 0:
            raise ValueError(f"El monto debe ser > 0, se recibió {monto}")

    def depositar(self, monto):
        self._validar_monto(monto)
        self.saldo += monto
        return self.saldo

    def retirar(self, monto):
        self._validar_monto(monto)
        if monto > self.saldo:
            return "Saldo insuficiente"   
        self.saldo -= monto
        return self.saldo

    def transferir(self, monto, otra_cuenta):
        self._validar_monto(monto)
        if monto > self.saldo:
            return False                   
        self.saldo -= monto
        otra_cuenta.saldo += monto
        return True

    def obtener_saldo(self):
        return self.saldo
