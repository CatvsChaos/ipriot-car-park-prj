class CarPark:
    def __init__(self, location, capacity, plates, displays):
        self.location = location
        self.capacity = capacity
        self.plates = plates or []
        self.displays = displays or []

    def __str__(self):
        return f"Car park location : {self.location} \n Capacity : {self.capacity}"


