import sys
import os
import unittest

# Add the 'src' directory to the Python path so 'calculadora' can be imported
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from cuenta_bancaria import CuentaBancaria

class TestCalcular(unittest.TestCase):
    # TODO Adiciona tus pruebas unitarias aquí.
    # Ejemplo:   
    def test_calcularInteres(self):
        valor_esperado = 115.0
        mi_cuenta=CuentaBancaria("maria","8949t2",100,)
        valor_actual =mi_cuenta.calcularInteres()
        self.assertEqual(valor_esperado, valor_actual)

    def test_retirar(self):
        valor_esperado ="saldo insuficiente"
        mi_cuenta=CuentaBancaria("maria","8949t2",0)
        valor_actual =mi_cuenta.retirar(100)
        self.assertEqual(valor_esperado, valor_actual)

if __name__ == '__main__':
    try:
        unittest.main()
    except SystemExit as e:
        print(f"Test results: {e.code}")

