import unittest
import cryptography_ui as crypts

# ---------------- SMALL TESTS ----------------

class Test_Miller_Rabin(unittest.TestCase):

    def test_small_primes(self):
        primes = [2, 3, 5, 7, 11, 13, 17, 19, 23]

        for p in primes:
            with self.subTest(p=p):
                self.assertTrue(crypts.miller_rabin(p))

    def test_small_composites(self):
        composites = [0, 1, 4, 6, 8, 9, 10, 12, 15, 21, 25]

        for n in composites:
            with self.subTest(n=n):
                self.assertFalse(crypts.miller_rabin(n))

    # ---------------- Additional Prime Tests ----------------

    def test_medium_primes(self):
        primes = [29, 31, 37, 41, 43, 47, 53, 59, 61]

        for p in primes:
            with self.subTest(p=p):
                self.assertTrue(crypts.miller_rabin(p))

    def test_large_primes(self):
        primes = [97, 101, 127, 257, 521, 607, 1021]

        for p in primes:
            with self.subTest(p=p):
                self.assertTrue(crypts.miller_rabin(p))

    def test_mersenne_and_special_primes(self):
        primes = [8191, 131071, 524287]

        for p in primes:
            with self.subTest(p=p):
                self.assertTrue(crypts.miller_rabin(p))

    def test_large_known_primes(self):
        primes = [1009, 5003, 7919, 10007]

        for p in primes:
            with self.subTest(p=p):
                self.assertTrue(crypts.miller_rabin(p))

    # ---------------- Additional Composite Tests ----------------

    def test_medium_composites(self):
        composites = [27, 33, 35, 39, 49, 51, 55, 57, 65]

        for n in composites:
            with self.subTest(n=n):
                self.assertFalse(crypts.miller_rabin(n))

    def test_even_composites(self):
        composites = [14, 16, 18, 20, 22, 24, 26, 28, 30]

        for n in composites:
            with self.subTest(n=n):
                self.assertFalse(crypts.miller_rabin(n))

    def test_carmichael_numbers(self):
        # These are composite but can fool Fermat primality tests.
        composites = [561, 1105, 1729, 2465, 2821, 6601]

        for n in composites:
            with self.subTest(n=n):
                self.assertFalse(crypts.miller_rabin(n))

    def test_large_composites(self):
        composites = [1001, 1025, 2047, 4095, 6600, 10000]

        for n in composites:
            with self.subTest(n=n):
                self.assertFalse(crypts.miller_rabin(n))
                

class TestRSA_small(unittest.TestCase):

    # ---------------- euclid_gcd ----------------

    def test_euclid_gcd(self):
        self.assertEqual(crypts.euclid_gcd(48, 18), 6)

    def test_euclid_gcd_2(self):
        self.assertEqual(crypts.euclid_gcd(54, 24), 6)

    def test_euclid_gcd_3(self):
        self.assertEqual(crypts.euclid_gcd(100, 25), 25)

    def test_euclid_gcd_4(self):
        self.assertEqual(crypts.euclid_gcd(17, 13), 1)

    def test_euclid_gcd_5(self):
        self.assertEqual(crypts.euclid_gcd(270, 192), 6)

    # ---------------- extended_gcd ----------------

    def test_extended_gcd(self):
        g, x, y = crypts.extended_gcd(101, 23)
        self.assertEqual(g, 101 * x + 23 * y)

    def test_extended_gcd_2(self):
        g, x, y = crypts.extended_gcd(48, 18)
        self.assertEqual(g, 48 * x + 18 * y)

    def test_extended_gcd_3(self):
        g, x, y = crypts.extended_gcd(99, 78)
        self.assertEqual(g, 99 * x + 78 * y)

    def test_extended_gcd_4(self):
        g, x, y = crypts.extended_gcd(35, 64)
        self.assertEqual(g, 35 * x + 64 * y)

    def test_extended_gcd_5(self):
        g, x, y = crypts.extended_gcd(270, 192)
        self.assertEqual(g, 270 * x + 192 * y)

    # ---------------- mod_inverse ----------------

    def test_mod_inverse(self):
        inv = crypts.mod_inverse(17, 3120)
        self.assertEqual((17 * inv) % 3120, 1)

    def test_mod_inverse_2(self):
        inv = crypts.mod_inverse(3, 11)
        self.assertEqual((3 * inv) % 11, 1)

    def test_mod_inverse_3(self):
        inv = crypts.mod_inverse(7, 40)
        self.assertEqual((7 * inv) % 40, 1)

    def test_mod_inverse_4(self):
        inv = crypts.mod_inverse(11, 26)
        self.assertEqual((11 * inv) % 26, 1)

    def test_mod_inverse_5(self):
        inv = crypts.mod_inverse(19, 1212)
        self.assertEqual((19 * inv) % 1212, 1)

    # ---------------- power_mod ----------------

    def test_power_mod(self):
        self.assertEqual(
            crypts.power_mod(7, 12345, 9973),
            pow(7, 12345, 9973)
        )

    def test_power_mod_2(self):
        self.assertEqual(
            crypts.power_mod(2, 100, 13),
            pow(2, 100, 13)
        )

    def test_power_mod_3(self):
        self.assertEqual(
            crypts.power_mod(5, 999, 97),
            pow(5, 999, 97)
        )

    def test_power_mod_4(self):
        self.assertEqual(
            crypts.power_mod(123, 456, 789),
            pow(123, 456, 789)
        )

    def test_power_mod_5(self):
        self.assertEqual(
            crypts.power_mod(9999, 8888, 10007),
            pow(9999, 8888, 10007)
        )

    # ---------------- string conversion ----------------

    def test_string_conversion(self):
        s = "Hello RSA world!"
        self.assertEqual(crypts.int_to_string(crypts.string_to_int(s)), s)

    def test_string_conversion_2(self):
        s = "ABC! DO RE MI! 123!"
        self.assertEqual(crypts.int_to_string(crypts.string_to_int(s)), s)

    def test_string_conversion_3(self):
        s = "Do Re Mi Fa So La Ti"
        self.assertEqual(crypts.int_to_string(crypts.string_to_int(s)), s)

    def test_string_conversion_4(self):
        s = "Once upon a time, in a land far away..."
        self.assertEqual(crypts.int_to_string(crypts.string_to_int(s)), s)

    def test_string_conversion_5(self):
        s = "S@ndi s#lls $ea$hells & scuba d!ving g3ar on the (sea)shore**"
        self.assertEqual(crypts.int_to_string(crypts.string_to_int(s)), s)

    # ---------------- choose_e ----------------

    def test_choose_e(self):
        e = crypts.choose_e(3120)
        self.assertEqual(crypts.gcd(e, 3120), 1)

    def test_choose_e_2(self):
        e = crypts.choose_e(120)
        self.assertEqual(crypts.gcd(e, 120), 1)

    def test_choose_e_3(self):
        e = crypts.choose_e(840)
        self.assertEqual(crypts.gcd(e, 840), 1)

    def test_choose_e_4(self):
        e = crypts.choose_e(1000)
        self.assertEqual(crypts.gcd(e, 1000), 1)

    def test_choose_e_5(self):
        e = crypts.choose_e(65520)
        self.assertEqual(crypts.gcd(e, 65520), 1)



# ---------------- LARGE TESTS ----------------

class TestRSA_main(unittest.TestCase):

    def test_miller_rabin_large(self):
        p1 = 170141183460469231731687303715884105727
        p2 = 2^521 - 1

        self.assertTrue(crypts.miller_rabin(p1))
        self.assertTrue(crypts.miller_rabin(p2))

        self.assertFalse(crypts.miller_rabin(p1 * p1))
        self.assertFalse(crypts.miller_rabin(p1 * p2))
        self.assertFalse(crypts.miller_rabin(p2 * p2))
    
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
        s = ("RSA cryptosystem is a family of public-key cryptosystems, widely used for secure data "
             "transmission. RSA stands for Rivest-Shamir-Adleman, the people who publicly described "
             "the algorithm in 1977.")
        self.assertEqual(crypts.int_to_string(crypts.string_to_int(s)), s)

    def test_choose_e(self):
        phi = 123456789123456789123456789123456789123456789123456789123456789123456789123457
        e = crypts.choose_e(phi)
        self.assertEqual(crypts.gcd(e, phi), 1)
