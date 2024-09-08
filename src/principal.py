from cuenta_bancaria import CuentaBancaria
if __name__ == '__main__':
    cuantaBancaria=CuentaBancaria("maria","8949t2",100)

    print(cuantaBancaria.__str__())

    print("el interes es "+str(cuantaBancaria.calcularInteres()))

    print("su saldo es "+str(cuantaBancaria.retirar(200)))

    