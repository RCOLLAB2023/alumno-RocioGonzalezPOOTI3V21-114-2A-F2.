class CuentaBancaria:
    def __init__(self,numeroCuenta,titular,saldo_inicial=0):
        self.numeroCuenta=numeroCuenta
        self.titular=titular
        self.saldo=saldo_inicial

    def depositar(self,monto):
        if monto > 0:
            self.saldo += monto
            print(f"Deposito exitoso de ${monto}")
        else:
            print("el monto a depositar debe ser positivo")

    def retirar (self,monto):
        if monto <= 0:
            print("elmonto a retirar debe ser positivo")
        elif monto > self.saldo:
            print("Fondos insuficientes")    
        else:
            self.saldo-= monto
            print(f"Retiro exitoso de ${monto}")    


            