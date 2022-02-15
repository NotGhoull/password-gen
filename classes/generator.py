class Generator:
    def generate_pass(length:int) -> str:
        """Generates a password

        Args:
            length (int): The length of the password to be generated

        Returns:
            str: the password in a string format
        """

        #? Import random
        import random

        #? Create a list of characters
        alphabet = "abcdefghijklmnopqrstuvwxyz"
        upper_alphabet = alphabet.upper()

        #? Create a list of numbers
        numbers = "0123456789"

        #? Create a list of special characters
        special_characters = "!@#$%^&*()_+"

        return "".join(
            random.choice(alphabet + upper_alphabet + numbers + special_characters)
            for _ in range(length)
        )
