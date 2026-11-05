class Garage:
    def __init__(self):
        self.vehicles = []

    def add_vehicle(self, vehicle):
        self.vehicles.append(vehicle)

    def remove_vehicle(self, vehicle):
        if vehicle not in self.vehicles:
            raise ValueError("Транспортного средства нет в гараже")
        self.vehicles.remove(vehicle)

    def show_all(self):
        for vehicle in self.vehicles:
            print(vehicle)

    def find_by_brand(self, brand):
        return [
            vehicle for vehicle in self.vehicles
            if vehicle.brand.lower() == brand.lower()
        ]
