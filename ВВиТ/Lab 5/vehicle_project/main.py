from garage import Garage
from models.bus import Bus
from models.car import Car
from models.motorcycle import Motorcycle
from models.truck import Truck
from models.vehicle import Vehicle


def main():
    print("--- Независимое состояние объектов ---")
    car1 = Car("Toyota", "Camry", 2024, 4)
    car2 = Car("Honda", "Civic", 2022, 4)
    car1.accelerate(60)
    print("Скорость car1:", car1.speed)
    print("Скорость car2:", car2.speed)

    print("--- Методы accelerate, brake, stop ---")
    car1.accelerate(20)
    print("После accelerate(20):", car1.speed)
    car1.brake(30)
    print("После brake(30):", car1.speed)
    car1.brake(500)
    print("После brake(500):", car1.speed)
    car1.accelerate(40)
    car1.stop()
    print("После stop():", car1.speed)

    print("--- Свойство speed ---")
    try:
        car1.speed = -10
    except ValueError as error:
        print("Ошибка:", error)

    print("--- Метод __str__ ---")
    print(car2)

    print("--- Абстрактный класс ---")
    try:
        Vehicle("Test", "Test", 2000)
    except TypeError as error:
        print("Ошибка:", error)

    print("--- Полиморфизм ---")
    vehicles = [
        Car("Toyota", "Camry", 2024, 4),
        Truck("Volvo", "FH16", 2021, 25),
        Motorcycle("Harley-Davidson", "Sportster", 2020, False),
        Bus("MAN", "Lion's City", 2023, 45, "24"),
    ]
    for vehicle in vehicles:
        print(vehicle.move())
        print(vehicle.get_info())

    print("--- Гараж ---")
    garage = Garage()
    for vehicle in vehicles:
        garage.add_vehicle(vehicle)
    garage.show_all()

    print("--- Поиск по марке Volvo ---")
    for vehicle in garage.find_by_brand("Volvo"):
        print(vehicle.get_info())

    print("--- Удаление из гаража ---")
    garage.remove_vehicle(vehicles[0])
    garage.show_all()


if __name__ == "__main__":
    main()
