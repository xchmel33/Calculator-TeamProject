from unittest import TestCase

class testcalc(TestCase):
    def test_subtraction(self):
        from calc import subtraction
        expression = ['6','-','6']
        expected = ['6','+',-6.0]
        expression = subtraction(expression)
        print(expression)
        print(expected)
        self.assertEqual(expression, expected)


