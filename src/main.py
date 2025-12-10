from car_park import CarPark
from pathlib import Path
from sensor import EntrySensor, ExitSensor
from display import Display


class Main:
    def __init__(self):
        # Create a car park object with the location moondalup, capacity 100, and log_file "moondalup.txt"
        self.car_park = CarPark("11 Appollo Drive", 100, [], [], [], log_file = Path("moondalup.txt"), config_file = Path("moondalup_config.json"))
        # Write the car park configuration to a file called "moondalup_config.json"
        self.car_park.write_config()
        # Reinitialize the car park object from the "moondalup_config.json" file
        self.car_park = CarPark.from_config(Path("moondalup_config.json"))

        # Create an entry sensor object with id 1, is_active True, and car_park car_park
        self.entry_sensor = EntrySensor(id=1, is_active=True, car_park=self.car_park)
        # Create an exit sensor object with id 2, is_active True, and car_park car_park
        self.exit_sensor = ExitSensor(id=2, is_active=True, car_park=self.car_park)

        # Create a display object with id 1, message "Welcome to Moondalup", is_on True, and car_park car_park
        self.display = Display(id=1, message="Welcome to Moondalup Car Park", is_on=True)

        # Drive 10 cars into the car park (must be triggered via the sensor - NOT by calling car_park.add_car directly)
        for i in range(10):
            self.entry_sensor.detect_vehicle()
            print(self.display)
            print(self.car_park)

        # Drive 2 cars out of the car park (must be triggered via the sensor - NOT by calling car_park.remove_car directly)
        for i in range(2):
            self.exit_sensor.detect_vehicle()
            print(self.display)
            print(self.car_park)

if __name__ == "__main__":
    Main()
