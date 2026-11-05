from models.vehicle import Vehicle


class Motorcycle(Vehicle):
    def __init__(self, brand, model, year, has_sidecar):
        super().__init__(brand, model, year)
        self.has_sidecar = has_sidecar

    def get_info(self):
        sidecar = "с коляской" if self.has_sidecar else "без коляски"
        return f"Мотоцикл: {super().get_info()}, {sidecar}"

    def move(self):
        return "Мотоцикл мчится по дороге"
