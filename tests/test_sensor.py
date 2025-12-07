import unittest
import car_park
import sensor

class TestSensor(unittest.TestCase):
    def setUp(self):
        self.car_park = car_park.CarPark("123 Example Street", 100, [], [], [])
        self.entry_sensor = sensor.EntrySensor(1, False, self.car_park)
        self.exit_sensor = sensor.ExitSensor(1, True, self.car_park)

    def test_entry_sensor_initialized_with_all_attributes(self):
        self.assertIsInstance(self.entry_sensor, sensor.Sensor)
        self.assertEqual(self.entry_sensor.id, 1)
        self.assertEqual(self.entry_sensor.is_active, False)
        self.assertEqual(self.entry_sensor.car_park, self.car_park)

    def test_exit_sensor_initialized_with_all_attributes(self):
        self.assertIsInstance(self.exit_sensor, sensor.Sensor)
        self.assertEqual(self.exit_sensor.id, 1)
        self.assertEqual(self.exit_sensor.is_active, True)
        self.assertEqual(self.exit_sensor.car_park, self.car_park)

    def test_detect_vehicle(self):
        self.entry_sensor.detect_vehicle()
        self.exit_sensor.detect_vehicle()
