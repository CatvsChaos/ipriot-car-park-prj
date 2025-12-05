class Display:
    def __init__(self, id, message, is_on):
        self.id = id
        self.message = ""
        self.is_on = False

    def __str__(self):
        return f"Display {self.id}: Welcome to the car park."
