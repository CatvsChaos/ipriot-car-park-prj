import unittest
from sensor import Sensor
from entry_sensor import EntrySensor
from exit_sensor import ExitSensor
from car_park import CarPark

class TestSensor(unittest.TestCase):
    def setUp(self):
        self.sensor = Sensor(1, False, CarPark("123 Example Street", 100, [], []))

    def test_sensor_initialized_with_all_attributes(self):
        self.assertEqual(self.sensor.id, 1)
        self.assertEqual(self.Sensor.is_active, False)
        # self.assertEqual(self.sensor.car_park, CarPark( "123 Example Street", 100, [], []))
        self.assertEqual(self.sensor.car_park, car_park)

    def test_detect_vehicle(self):
        self.assertEqual(self.sensor.entry_sensor.plate, "FAKE-001")
        self.assertEqual(self.sensor.entry_sensor)


    # class Sensor(ABC):
    #     def __init__(self, id, is_active, car_park):
    #         self.id = id
    #         self.is_active = is_active
    #         self.car_park = car_park

        # def detect_vehicle(self):
        #     plate = self._scan_plate()
        #     self.update_car_park(plate)