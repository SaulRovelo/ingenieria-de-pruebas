# cuenta.py
class CuentaBancaria:
    def __init__(self, titular, saldo=0):
        self.titular = titular
        self.saldo = saldo

    def depositar(self, monto):
        if monto <= 0:
            return "Monto inválido"
        self.saldo += monto
        return self.saldo

    def retirar(self, monto):
        if monto <= 0:
            return "Monto inválido"
        if monto > self.saldo:
            return "Saldo insuficiente"
        self.saldo -= monto
        return self.saldo

    def transferir(self, monto, otra_cuenta):
        if monto <= 0 or monto > self.saldo:
            return False
        self.saldo -= monto
        otra_cuenta.saldo += monto
        return True

    def obtener_saldo(self):
        return self.saldo
