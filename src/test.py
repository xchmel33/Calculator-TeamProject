from unittest import TestCase


class Test_Calculations(TestCase):
    def test_addition(self):
        from calc import addition
        self.assertEqual(addition(['0', '+', '3']), [3])
        self.assertEqual(addition(['-3', '+', '0']), [-3])
        self.assertEqual(addition(['9.11', '+', '-0.11']), [9])

        self.assertNotEqual(addition(['-3', '+', '-3']), [0])
        self.assertNotEqual(addition(['2.2', '+', '1']), [3])


    def test_subtraction(self):
        from calc import subtraction
        self.assertEqual(subtraction(['-', '3', '+', '2']), [-3, '+', '2'])
        self.assertEqual(subtraction(['2', '-', '3']), ['2', '+', -3])
        self.assertEqual(subtraction(['2.1', '*', '-', '3.1']), ['2.1', '*', -3.1])

        self.assertNotEqual(subtraction(['-', '3', '-', '3']), ['-3', '-', '3'])
        self.assertNotEqual(subtraction(['2.2', '-', '1.1']), ['2.2', '-', '-1.1'])


    def test_multiplication(self):
        from calc import multiplication
        self.assertEqual(multiplication(['0', '*', '4']), [0])
        self.assertEqual(multiplication(['3', '*', '-1']), [-3])
        self.assertEqual(multiplication(['-1.1', '*', '-1.1']), [1.21])

        self.assertNotEqual(multiplication(['-3', '*', '1']), [3])
        self.assertNotEqual(multiplication(['2', '*', '0']), [2])


    def test_division(self):
        from calc import division
        self.assertEqual(division(['0', '/', '4']), [0])
        self.assertEqual(division(['-1.0', '/', '4.0']), [-0.25])

        self.assertNotEqual(division(['-4', '/', '2']), [2])
        self.assertNotEqual(division(['-1', '/', '-5']), [-0.2])

        self.assertRaises(ValueError, division, ['7','/','0'])


    def test_factorial(self):
        from calc import factorial
        self.assertEqual(factorial(['0', '!']), [1])
        self.assertEqual(factorial(['5', '!']), [120])

        self.assertNotEqual(factorial(['9', '!']), [9])
        self.assertNotEqual(factorial(['0', '!']), [0])

        self.assertRaises(ValueError, factorial, ['-2','!'])


    def test_power(self):
        from calc import power
        self.assertEqual(power(['2', '^', '4']), [16])
        self.assertEqual(power(['9', '^', '0']), [1])
        self.assertEqual(power(['1.23', '^', '3']), [1.860867])

        self.assertNotEqual(power(['-3', '^', '3']), [27])
        self.assertNotEqual(power(['27', '^', '0']), [27])


    def test_root(self):
        from calc import root
        self.assertEqual(root(['3', 'r', '-27']), [-3])
        self.assertAlmostEqual(root(['2', 'r', '2.0']), [1.4142135623730951])

        self.assertNotEqual(root(['3', 'r', '-27']), [3])
        self.assertNotEqual(root(['2', 'r', '2']), [2])

        self.assertRaises(ValueError, root, ['2','r','-4'])
        self.assertRaises(ValueError, root, ['-2','r','4'])


    def test_logarithm(self):
        from calc import logarithm
        self.assertEqual(logarithm(['l','o','g','1']), [0])
        self.assertEqual(logarithm(['l','o','g','4.5']),[0.6532125137753436])
        self.assertEqual(logarithm(['l','o','g','10']),[1])

        self.assertNotEqual(logarithm(['l','o','g','10']),[10])
        self.assertNotEqual(logarithm(['l','o','g','1000']),[1000])

class Test_Other(TestCase):
    def test_maxparenthesis(self):
        from calc import max_parenthesis
        self.assertEqual(max_parenthesis(['(','5','*','8',')']), 1)
        self.assertEqual(max_parenthesis(['(','(','-2',')',')']), 2)
        self.assertEqual(max_parenthesis(['6','+','-15','*','1']), 0)

        self.assertRaises(ValueError, max_parenthesis, [')','5','*','8',')'])
        self.assertRaises(ValueError, max_parenthesis, ['(','5','*','8',')',')'])
        self.assertRaises(ValueError, max_parenthesis, ['6','*','20',')','8',])

    def test_calcparenthesis(self):
        from calc import calc_parenthesis
        self.assertEqual(calc_parenthesis(['(','5','*','8',')'],1), [40])
        self.assertEqual(calc_parenthesis(['(','4','+','9',')','*','10'],1), [13,'*','10'])

        self.assertNotEqual(calc_parenthesis(['10','(','15','+','95',')'],1), [1100])

    def test_calcinside(self):
        from calc import calc_inside
        self.assertEqual(calc_inside(['7','+','5','*','4']), 27)
        self.assertEqual(calc_inside(['54','-','12','/','4']), 51)
        self.assertEqual(calc_inside(['l','o','g','100','*','r','16']), 8)

        self.assertNotEqual(calc_inside(['2', 'r', '2','+','8']), 2)
        self.assertNotEqual(calc_inside(['8', '-', '40','/','8']), 4)
