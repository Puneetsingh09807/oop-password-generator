import random
import string

class PasswordGenerator:
    def __init__(self, length=8, use_upper=True, use_lower=True, use_digits=True, use_symbols=True):
        self.length = length
        self.use_upper = use_upper
        self.use_lower = use_lower
        self.use_digits = use_digits
        self.use_symbols = use_symbols

    def _build_character_pool(self):
        pool = ""
        if self.use_lower:
            pool += string.ascii_lowercase
        if self.use_upper:
            pool += string.ascii_uppercase
        if self.use_digits:
            pool += string.digits
        if self.use_symbols:
            pool += string.punctuation

        return pool

    def generate_password(self):
        pool = self._build_character_pool()

        if not pool:
            return "Error: No character set selected!"

        password = ''.join(random.choice(pool) for _ in range(self.length))
        return password

    def check_strength(self, password):
        score = 0

        if any(c.islower() for c in password):
            score += 1
        if any(c.isupper() for c in password):
            score += 1
        if any(c.isdigit() for c in password):
            score += 1
        if any(c in string.punctuation for c in password):
            score += 1

        if len(password) >= 12:
            score += 1

        if score <= 2:
            return "Weak"
        elif score == 3 or score == 4:
            return "Medium"
        else:
            return "Strong"


# -------- Main Program --------
if __name__ == "__main__":
    print("=== Password Generator ===")

    length = int(input("Enter password length: "))
    use_upper = input("Include uppercase? (y/n): ") == 'y'
    use_lower = input("Include lowercase? (y/n): ") == 'y'
    use_digits = input("Include numbers? (y/n): ") == 'y'
    use_symbols = input("Include symbols? (y/n): ") == 'y'

    generator = PasswordGenerator(length, use_upper, use_lower, use_digits, use_symbols)

    password = generator.generate_password()
    strength = generator.check_strength(password)

    print("\nGenerated Password:", password)
    print("Strength:", strength)
