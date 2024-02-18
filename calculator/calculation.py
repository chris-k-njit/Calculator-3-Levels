class Calculation:
    def __init__(self, x, y, operation):
        self.x = x
        self.y = y
        self.operation = operation  # Store the operation function

    def get_result(self):
        # Call the stored operation with x and y
        # Testing Professors code for part 2, making my own for part 3
        return self.operation(self.x, self.y)