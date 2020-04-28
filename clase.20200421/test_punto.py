import unittest
from punto import Punto2D, PuntoMejorado

class TestPunto(unittest.TestCase):
    def test_str_punto(self):
        punto = Punto2D(4, 5)
        self.assertEqual(punto, "(4, 5)")

if __name__ == "__main__":
    unittest.main()
