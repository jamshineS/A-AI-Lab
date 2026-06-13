import unittest
import crypts   

class TestRSA_small(unittest.TestCase):

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






class TestRSA_main(unittest.TestCase):

    def test_euclid_gcd(self):
        a = 9876543219876543219876543219876543219876
        b = 1234567891234567891234567891234567891234
        self.assertEqual(crypts.euclid_gcd(a, b), 2)

    def test_extended_gcd(self):
        a = 99999999999999999999999999999999999999991
        b = 88888888888888888888888888888888888888889
        g, x, y = crypts.extended_gcd(a, b)
        self.assertEqual(g, a*x + b*y)

    def test_mod_inverse(self):
        a = 12345678912345678912345678912345678912345
        m = 98765432198765432198765432198765432198767
        inv = crypts.mod_inverse(a, m)
        self.assertEqual((a * inv) % m, 1)

    def test_power_mod(self):
        base = 123456789123456789123456789123456789
        exp  = 987654321987654321987654321987654321
        mod  = 999999999999999999999999999999999937
        self.assertEqual(crypts.power_mod(base, exp, mod),
                         pow(base, exp, mod))

    def test_string_conversion(self):
        s = "RSA cryptosystem is a family of public-key cryptosystems, widely used for secure data transmission. RSA stands for Rivest-Shamir-Adleman, the peoplewho publicly described the algorithm in 1977."
        self.assertEqual(crypts.int_to_string(crypts.string_to_int(s)), s)

    def test_choose_e(self):
        phi = 123456789123456789123456789123456789123456789123456789123456789123456789123457
        e = crypts.choose_e(crypts.phi)
        self.assertEqual(crypts.gcd(e, crypts.phi), 1)
