from models.vehicle import Vehicle


class Bus(Vehicle):
    def __init__(self, brand, model, year, seats, route):
        super().__init__(brand, model, year)
        self.seats = seats
        self.route = route

    def get_info(self):
        return (
            f"Автобус: {super().get_info()}, "
            f"мест: {self.seats}, маршрут: {self.route}"
        )

    def move(self):
        return f"Автобус едет по маршруту {self.route}"
