class CuentaBancaria:
    def __init__(self,titular,numeroCuenta,saldo):
        self._titular=titular
        self._numeroCuenta=numeroCuenta
        self._saldo=saldo
        self._tipoInteres=15
    
    def get_titular(self):
        return self._titular
    
    def set_titular(self,titular):
        self._titular=titular
    
    def get_numeroCuenta(self):
        return self._numeroCuenta
    
    def get_saldo(self):
        return self._saldo
    
    def set_tipoInteres(self, tipoInteres):
        if tipoInteres <0 or tipoInteres >10:
            return print("interes invalido")
        else:   self._tipoInteres=tipoInteres

    def ingresar(self,ingreso):
       self.saldo+=ingreso

    def retirar(self,retirar):
        if retirar>self._saldo:
            return "saldo insuficiente"
        else :
            self._saldo-=retirar
            return self._saldo
    

    def calcularInteres(self):
        interes=self._saldo+(self._saldo*((self._tipoInteres/ 100)))
        return interes

    def __str__(self):
        return (f"Cuenta Bancaria\n"
                f"Titular: {self._titular}\n"
                f"Número de Cuenta: {self._numeroCuenta}\n"
                f"Saldo: {self._saldo:.2f}\n"
                f"Tipo de Interés: {self._tipoInteres}%")


