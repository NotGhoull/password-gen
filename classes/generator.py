class Generator:
    def generate_pass(length:int) -> str:
        """Generates a password

        Args:
            length (int): The length of the password to be generated

        Returns:
            str: the password in a string format
        """

        import random
        alphabet = "abcdefghijklmnopqrstuvwxyz"
        upper_alphabet = alphabet.upper()
        numbers = "0123456789"
        special_characters = "!@#$%^&*()_+"
        return "".join(
            random.choice(alphabet + upper_alphabet + numbers + special_characters)
            for _ in range(length)
        )
