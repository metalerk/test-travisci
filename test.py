from app import Operaciones
import unittest

class TestOperaciones(unittest.TestCase):
    def test_suma(self):
        num1 = 2
        num2 = 4
        self.assertEqual(Operaciones.suma(num1, num2), 6)
