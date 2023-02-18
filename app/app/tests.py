"""
Sample test
"""

from django.test import SimpleTestCase

from app.calc import add, substract


class CalcTest(SimpleTestCase):

    def test_add_numbers(self):
        """test add numbers"""
        res = add(5, 7)

        self.assertEqual(res, 12)

    def test_substract_numbers(self):
        """test substract numbers"""
        res = substract(10, 15)

        self.assertEqual(res, 5)
