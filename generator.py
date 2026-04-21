import random
import string

class PasswordGenerator:
    """A class to handle secure password generation logic."""
    
    def __init__(self, length=12, use_upper=True, use_digits=True, use_special=True):
        self.length = length
        self.use_upper = use_upper
        self.use_digits = use_digits
        self.use_special = use_special
        
        # Base character set (always lowercase)
        self.characters = string.ascii_lowercase

    def _build_char_pool(self):
        """Private method to assemble the pool of characters based on settings."""
        pool = self.characters
        if self.use_upper:
            pool += string.ascii_uppercase
        if self.use_digits:
            pool += string.digits
        if self.use_special:
            pool += string.punctuation
        return pool

    def generate(self):
        """Generates a random password from the built pool."""
        char_pool = self._build_char_pool()
        
        if not char_pool:
            raise ValueError("No characters available to generate a password.")

        password = "".join(random.choice(char_pool) for _ in range(self.length))
        return password
