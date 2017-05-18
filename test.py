from app import Operaciones
import unittest

class TestOperaciones(unittest.TestCase):
    def test_suma(self):
        num1 = 2
        num2 = 4
        self.assertEqual(Operaciones.suma(num1, num2), 6)

    def test_resta(self):
        num1 = 34
        num2 = 24
        self.assertEqual(Operaciones.resta(num1, num2), 10)
