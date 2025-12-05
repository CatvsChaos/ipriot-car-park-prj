class EntrySensor:
    def __init__(self):
        self.car_park = None

    def update_car_park(self, plate):
        self.car_park.add_car(plate)
        print(f"Incoming 🚘 vehicle detected. Plate: {plate}")