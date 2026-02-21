import secrets  
from sympy import isprime, mod_inverse  
from math import gcd      
import math
import random              


# ---------------- MILLER–RABIN PRIMALITY TEST ----------------

def miller_rabin(n, k = 100):
    """Return True if n is probably prime using the Miller–Rabin test."""
    
    if n == 2 or n == 3:        # Handle small primes
        return True
    if n <= 1 or n % 2 == 0:    # Reject negatives, 0, 1, and even numbers
        return False

    # Write n - 1 as 2^r * d (factor out powers of 2)
    r, d = 0, n - 1
    while d % 2 == 0:
        d //= 2
        r += 1

    # Perform k rounds of testing
    for _ in range(k):
        a = random.randint(2, n - 2)   # Random base
        x = pow(a, d, n)               # Compute a^d mod n

        if x == 1 or x == n - 1:       # Strong probable prime check
            continue

        # Repeat squaring step r - 1 times
        for _ in range(r - 1):
            x = pow(x, 2, n)
            if x == n - 1:             # If we hit -1 mod n, it's probably prime
                break
        else:
            return False               # Composite number

    return True                        # Probably prime


# ---------------- PRIME GENERATOR ----------------

def generate_large_prime(bits):
    """Generate a random prime number with the given bit length using Miller–Rabin."""
    while True:
        candidate = secrets.randbits(bits)   # Generate random number of given bit size
        candidate |= 1                       # Force odd number
        candidate |= (1 << (bits - 1))       # Ensure highest bit is 1 → correct bit length

        if miller_rabin(candidate):          # Test primality
            return candidate                 # Return when prime found
        
def candidate_is_prime(candidate):
    """Check if a candidate number is prime using Miller-Rabin test."""
    return miller_rabin(candidate, 1000)


# ---------------- RSA FUNCTIONS ----------------

def power_mod(base, exponent, modulus):
    """Efficient modular exponentiation (square-and-multiply)."""
    result = 1
    b = base % modulus
    while exponent > 0:
        if exponent & 1:                     # If lowest bit is 1, multiply
            result = (result * b) % modulus
        exponent >>= 1                       # Shift exponent right by 1 bit
        b = (b * b) % modulus                # Square base each round
    return result

def choose_e(phi):
    """Choose a public exponent e that is coprime with phi."""
    e = 65537                                # Standard RSA public exponent
    if gcd(e, phi) == 1:
        return e
    e = 3                                    # Fallback: try odd numbers
    while gcd(e, phi) != 1:
        e += 2
    return e

def string_to_int(s):
    """Convert a string into an integer."""
    return int.from_bytes(s.encode(), byteorder='little')

def int_to_string(i):
    """Convert an integer back into a string."""
    length = math.ceil(i.bit_length() / 8)
    return i.to_bytes(length, byteorder='little').decode()


# ---------------- RSA SETUP ----------------

bits = 2000                                  # RSA prime size (2000-bit primes)

print("Generating 2000-bit primes... this may take a moment.")

p = generate_large_prime(bits)               # First large prime
q = generate_large_prime(bits)               # Second large prime

n = p * q                                    # RSA modulus
phi = (p - 1) * (q - 1)                      # Euler's totient
e = choose_e(phi)                            # Public exponent
d = mod_inverse(e, phi)                      # Private exponent (modular inverse)

print("Keys generated successfully.\n")


# ---------------- ENCRYPTION ----------------

message_str = input("Enter a message: ")     # User input
message = string_to_int(message_str)         # Convert message to integer

if message >= n:                             # Ensure message fits in modulus
    raise ValueError("Message too large for RSA modulus. Use a shorter message.")

print("\nPublic key component (e):", e)
entered_e = int(input("Enter the public key component: "))

if entered_e != e:                           # Simple correctness check
    raise ValueError("Incorrect public key component.")

cipher = power_mod(message, e, n)            # Encrypt message


# ---------------- DECRYPTION ----------------

print("\nPrivate key component (d):", d)
entered_d = int(input("Enter the private key component: "))

if entered_d != d:                           # Check private key correctness
    raise ValueError("Incorrect private key component.")

decrypted_int = power_mod(cipher, d, n)      # Decrypt ciphertext
decrypted = int_to_string(decrypted_int)     # Convert back to string


# ---------------- OUTPUT ----------------

print("\nCiphertext:", cipher)
print("Decrypted message:", decrypted)

