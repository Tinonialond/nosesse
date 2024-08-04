class BitwardenError(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)

class InvalidCredentialsError(BitwardenError):
    def __init__(self, message="Invalid username or password"):
        super().__init__(message)

class ItemNotFoundError(BitwardenError):
    def __init__(self, message="Item not found"):
        super().__init__(message)

# Add more custom exceptions as needed
