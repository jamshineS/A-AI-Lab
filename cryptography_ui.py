import secrets
import math
import random
from math import gcd


#  __________________________ SIEVE OF ERATOSTHENES — FIRST 1000 PRIMES FOR PRUNING __________________________

def sieve_of_eratosthenes(limit):
    sieve = [True] * (limit + 1)
    sieve[0] = sieve[1] = False

    for num in range(2, int(math.sqrt(limit)) + 1):
        if sieve[num]:
            for multiple in range(num * num, limit + 1, num):
                sieve[multiple] = False

    return [i for i, prime in enumerate(sieve) if prime]

SMALL_PRIMES = sieve_of_eratosthenes(10000)[:1000]


#  __________________________ MILLER–RABIN PRIMALITY TEST __________________________

def miller_rabin(n, k=40):
    if n in (2, 3):
        return True
    if n <= 1 or n % 2 == 0:
        return False

    r, d = 0, n - 1
    while d % 2 == 0:
        d //= 2
        r += 1

    for _ in range(k):
        a = random.randint(2, n - 2)
        x = pow(a, d, n)

        if x == 1 or x == n - 1:
            continue

        for _ in range(r - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                break
        else:
            return False

    return True


#  __________________________ PRIME GENERATOR WITH SIEVE PRUNING __________________________

def candidate_is_prime(candidate):
    # 1) Trial division by first 1000 primes
    for p in SMALL_PRIMES:
        if p * p > candidate:
            break
        if candidate % p == 0:
            return False

    # 2) Miller–Rabin
    return miller_rabin(candidate, k=40)


def generate_large_prime(bits):
    while True:
        candidate = secrets.randbits(bits)
        candidate |= 1
        candidate |= (1 << (bits - 1))

        if candidate_is_prime(candidate):
            return candidate


#  __________________________ EXTENDED EUCLIDEAN + MODULAR INVERSE __________________________

def euclid_gcd(a, b):
    while b:
        a, b = b, a % b
    return a


def extended_gcd(a, b):
    if b == 0:
        return (a, 1, 0)
    g, x1, y1 = extended_gcd(b, a % b)
    return (g, y1, x1 - (a // b) * y1)


def mod_inverse(a, m):
    g, x, _ = extended_gcd(a, m)
    if g != 1:
        raise ValueError("No modular inverse exists")
    return x % m


#  __________________________ RSA UTILITY FUNCTIONS __________________________

def power_mod(base, exponent, modulus):
    result = 1
    b = base % modulus
    while exponent > 0:
        if exponent & 1:
            result = (result * b) % modulus
        exponent >>= 1
        b = (b * b) % modulus
    return result


def choose_e(phi):
    e = 65537
    if gcd(e, phi) == 1:
        return e
    e = 3
    while gcd(e, phi) != 1:
        e += 2
    return e


def string_to_int(s):
    return int.from_bytes(s.encode(), "little")


def int_to_string(i):
    length = math.ceil(i.bit_length() / 8)
    return i.to_bytes(length, "little").decode()


#  __________________________ FUNCTION TEST SUITE __________________________

def functions_check():
    """Backend only. Raises errors if something is wrong."""
    
    # Test Euclidean GCD
    assert euclid_gcd(48, 18) == 6

    # Test extended GCD consistency
    g, x, y = extended_gcd(101, 23)
    assert g == 101 * x + 23 * y

    # Test modular inverse
    inv = mod_inverse(17, 3120)
    assert (17 * inv) % 3120 == 1

    # Test power_mod vs built-in pow
    assert power_mod(7, 12345, 9973) == pow(7, 12345, 9973)

    # Test string conversion round-trip
    s = "Hello RSA"
    assert int_to_string(string_to_int(s)) == s

    # Test choose_e
    e = choose_e(3120)
    assert gcd(e, 3120) == 1

    # If we reach here, everything is OK
    return True



#  __________________________ RSA KEY GENERATION + ENCRYPTION + DECRYPTION __________________________

if __name__ == "__main__":
    functions_check()

    bits = 1024  # use 1024 for speed; change to 2000 later

    print("Generating primes...")
    p = generate_large_prime(bits)
    q = generate_large_prime(bits)

    n = p * q
    phi = (p - 1) * (q - 1)
    e = choose_e(phi)
    d = mod_inverse(e, phi)

    print("\nKeys generated successfully.\n")

    # ---------------- ENCRYPTION ----------------

    message_str = input("Enter a message: ")
    m = string_to_int(message_str)

    if m >= n:
        raise ValueError("Message too large for RSA modulus.")

    print("\nPublic key component (e):", e)
    entered_e = int(input("Enter the public key component: "))

    if entered_e != e:
        raise ValueError("Incorrect public key component.")

    cipher = power_mod(m, e, n)

    # ---------------- DECRYPTION ----------------

    print("\nPrivate key component (d):", d)
    entered_d = int(input("Enter the private key component: "))

    if entered_d != d:
        raise ValueError("Incorrect private key component.")

    decrypted = int_to_string(power_mod(cipher, d, n))

    # ---------------- OUTPUT ----------------

    print("\nCiphertext:", cipher)
    print("Decrypted message:", decrypted)
