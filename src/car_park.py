class CarPark:
    def __init__(self, location, capacity, plates, displays):
        self.location = location
        self.capacity = capacity
        self.plates = plates or []
        self.displays = displays or []

