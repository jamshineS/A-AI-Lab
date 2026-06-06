import unittest
import crypts   # import your RSA module

class TestRSA(unittest.TestCase):

    def test_euclid_gcd(self):
        self.assertEqual(crypts.euclid_gcd(48, 18), 6)

    def test_extended_gcd(self):
        g, x, y = crypts.extended_gcd(101, 23)
        self.assertEqual(g, 101 * x + 23 * y)

    def test_mod_inverse(self):
        inv = crypts.mod_inverse(17, 3120)
        self.assertEqual((17 * inv) % 3120, 1)

    def test_power_mod(self):
        self.assertEqual(crypts.power_mod(7, 12345, 9973), pow(7, 12345, 9973))

    def test_string_conversion(self):
        s = "Hello RSA world!"
        self.assertEqual(crypts.int_to_string(crypts.string_to_int(s)), s)

    def test_choose_e(self):
        e = crypts.choose_e(3120)
        self.assertEqual(crypts.gcd(e, 3120), 1)
