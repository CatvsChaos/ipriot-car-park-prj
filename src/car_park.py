from sensor import Sensor
from display import Display

class CarPark:
    def __init__(self, location, capacity, plates, sensors, displays):
        self.location = location
        self.capacity = capacity
        self.plates = plates or []
        self.sensors = sensors or []
        self.displays = displays or []

    def __str__(self):
        return f"Car park location : {self.location} \n Capacity : {self.capacity}"

    def register(self, component):
        if not isinstance(component, (Sensor, Display)):
            raise TypeError("Object must be a Sensor or Display")

        if isinstance(component, Sensor):
            self.sensors.append(component)
        elif isinstance(component, Display):
            self.displays.append(component)

    def add_car(self, plate):
        self.plates.append(plate)
        self.update_displays()

    def remove_car(self, plate):
        self.plates.remove(plate)
        self.update_displays()

    @property
    def available_bays(self):
        # 2.7.3.1 Detour: Implement available bays.
        # Use operator == so that when last plate takes last bay,
        # display shows 0 capacity and driver is notified.
        if len(self.plates) == max(self.capacity):
            return 0
        else:
            return self.capacity - len(self.plates)

    def update_displays(self):

        data = {"available bays": self.available_bays, "temperature": 25}

        for display in self.displays:
            display.update(data)



