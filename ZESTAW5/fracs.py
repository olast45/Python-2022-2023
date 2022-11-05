import math
import unittest


class TestFractions(unittest.TestCase):
    def setUp(self):
        self.zero = [0, 1]

    def test_add_frac(self):
        self.assertEqual(add_frac([1, 2], [1, 3]), [5, 6])
        self.assertEqual(add_frac([4, 9], [-1, 3]), [1, 9])

    def test_sub_frac(self):
        self.assertEqual(sub_frac([-2, 3], [-1, 2]), [-1, 6])
        self.assertEqual(sub_frac([0, 3], [-1, 2]), [1, 2])

    def test_mul_frac(self):
        self.assertEqual(mul_frac([5, 6], [7, 9]), [35, 54])
        self.assertEqual(mul_frac([1, 3], [-1, 2]), [-1, 6])

    def test_div_frac(self):
        self.assertEqual(div_frac([3, 8], [1, 2]), [3, 4])
        self.assertEqual(div_frac([-3, 78], [5, 8]), [-4, 65])

    def test_is_positive(self):
        self.assertEqual(is_positive([2, -1]), False)
        self.assertEqual(is_positive([2, 1]), True)

    def test_is_zero(self):
        self.assertEqual(is_zero([0, 5]), True)
        self.assertEqual(is_zero([1, 5]), False)

    def test_cmp_frac(self):
        self.assertEqual(cmp_frac([3, 5], [6, 10]), 0)
        self.assertEqual(cmp_frac([1, 2], [4, 10]), 1)

    def test_frac2float(self):
        self.assertEqual(frac2float([3, 7]), [3.0, 7.0])
        self.assertEqual(frac2float([5, 7]), [5.0, 7.0])

    def tearDown(self): pass


def simplest_form(num, den):
    frac = []
    greatest_common_divisor = math.gcd(num, den)
    numerator = int(num / greatest_common_divisor)
    denominator = int(den / greatest_common_divisor)
    frac.append(numerator)
    frac.append(denominator)
    if(frac[0] < 0) and (frac[1] < 0):
        frac[0] = abs(frac[0])
        frac[1] = abs(frac[1])
    else:
        pass
    return frac


def is_positive(frac):
    if (frac[0] < 0) or (frac[1] < 0):
        return False
    else:
        return True


def negative_fraction(frac):
    if frac[1] < 0:
        frac[1] = abs(frac[1])
        frac[0] = - frac[0]
    else:
        pass
    return frac


def sub_frac(frac1, frac2):
    greatest_common_divisor = math.gcd(frac1[1], frac2[1])
    frac1 = negative_fraction(frac1)
    frac2 = negative_fraction(frac2)
    zero(frac1)
    zero(frac2)
    denominator = int((frac1[1] * frac2[1]) / greatest_common_divisor)
    numerator = int((frac1[0] * (denominator / frac1[1])) - (frac2[0] * (denominator / frac2[1])))
    return simplest_form(numerator, denominator)


def add_frac(frac1, frac2):  # each fraction is given as a list [numerator, denominator]
    greatest_common_divisor = math.gcd(frac1[1], frac2[1])
    frac1 = negative_fraction(frac1)
    frac2 = negative_fraction(frac2)
    zero(frac1)
    zero(frac2)
    denominator = int((frac1[1] * frac2[1])/greatest_common_divisor)
    numerator = int((frac1[0] * (denominator/frac1[1])) + (frac2[0] * (denominator/frac2[1])))
    return simplest_form(numerator, denominator)


def mul_frac(frac1, frac2):
    frac1 = negative_fraction(frac1)
    frac2 = negative_fraction(frac2)
    zero(frac1)
    zero(frac2)
    denominator = frac1[1] * frac2[1]
    numerator = frac1[0] * frac2[0]
    return simplest_form(numerator, denominator)


def div_frac(frac1, frac2):
    frac1 = negative_fraction(frac1)
    frac2 = negative_fraction(frac2)
    zero(frac1)
    zero(frac2)
    denominator = frac1[1] * frac2[0]
    numerator = frac1[0] * frac2[1]
    return simplest_form(numerator, denominator)


def is_zero(frac):
    if (frac[0] == 0) and (frac[1] != 0):
        return True
    else:
        return False


def zero(frac):
    if frac[1] == 0:
        print('Division by 0!')
        exit(1)


def frac2float(frac):
    frac = negative_fraction(frac)
    zero(frac)
    res = [float(frac[0]), float(frac[1])]
    return res


def cmp_frac(frac1, frac2):
    frac1 = negative_fraction(frac1)
    frac2 = negative_fraction(frac2)
    zero(frac1)
    zero(frac2)
    new_frac1 = [frac1[0] * frac2[1], frac1[1] * frac2[1]]
    new_frac2 = [frac2[0] * frac1[1], frac1[1] * frac2[1]]
    if (new_frac1[0] == new_frac2[0]) and (new_frac1[1] == new_frac2[1]):
        return 0
    elif new_frac1[0] > new_frac2[0]:
        return 1
    return -1


if __name__ == '__main__':
    unittest.main()





