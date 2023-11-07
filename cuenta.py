class Cuenta:
    def __init__(self, numero, titular, saldo, limite):
        print("Construyendo el objeto...{}".format(self))
        self.numero = numero
        self.titular = titular
        self.saldo = saldo
        self.limite = limite
        
    def extracto(self):
        print('saldo {} del titular {}'.format(self.saldo, self.titular))
        
    def depositar(self, valor):
        self.saldo += valor
        
    def retirar(self, monto):
        if self.saldo >= monto:
            self.saldo -= monto
            print(f"Retiro exitoso. Saldo restante: ${self.saldo}")
        else:
            print("No tiene suficiente saldo para retirar.")