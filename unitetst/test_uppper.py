"""
Test de la funcion que retorna el string en mayuscula
"""

import unittest
from upper_function import upper_text


class TestUpperText(unittest.TestCase):

    def test_upper_text(self):
        word = "hola, mundo!"
        restul = upper_text(word)
        self.assertEqual(restul, "HOLA, MUNDO!")


if __name__ == "__main__":
    unittest.main()
