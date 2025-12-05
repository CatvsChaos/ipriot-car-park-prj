import random
from abc import ABC, abstractmethod

class Sensor(ABC):
    def __init__(self, id, is_active, car_park):
        self.id = id
        self.is_active = is_active
        self.car_park = car_park

    def __str__(self):
        return f"Sensor {self.id}: {self.is_active}"

    @abstractmethod
    def update_car_park(self, plate):
        pass

    def _scan_plate(self):
        return 'FAKE-' + format(random.randint(0,999), '03d')

    def detect_vehicle(self):
        plate = self._scan_plate()
        self.update_car_park(plate)

class EntrySensor(Sensor):
    pass

class ExitSensor(Sensor):
    pass

