class InvalidProportionalGainError(Exception):
    """Exception raised for errors in Proportional Gain (N).

    Attributes:
        N -- input Proportional Gain which caused the error
        message -- explanation of the error
    """
    def __init__(self, N, message="Proportional Gain is not above 0"):
        self.N = N
        self.message = message
        super().__init__(self.message)

class OutOfBoundsRangeError(Exception):
    """Exception raised for errors in range.

    Attributes:
        R -- input range which caused the error
        message -- explanation of the error
    """
    def __init__(self, R, message="Range is not greater than 0"):
        self.R = R
        self.message = message
        super().__init__(self.message)