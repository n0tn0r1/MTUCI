import json
import logging
from pathlib import Path

from utils.reader import read_numbers, validate_numbers
from utils.statistics import calculate_average, find_min, find_max

BASE_DIR = Path(__file__).resolve().parent
CONFIG_PATH = BASE_DIR / "config.json"


def load_config(config_path):
    """Загружает настройки из JSON-файла."""
    with open(config_path, "r", encoding="utf-8") as file:
        return json.load(file)


def setup_logging(log_file):
    """Настраивает запись журнала в файл."""
    log_path = BASE_DIR / log_file
    log_path.parent.mkdir(exist_ok=True)
    logging.basicConfig(
        filename=log_path,
        level=logging.INFO,
        format="%(asctime)s %(levelname)s %(message)s",
        encoding="utf-8",
    )


def main():
    print("Текущий рабочий каталог:", Path.cwd())

    try:
        config = load_config(CONFIG_PATH)
    except FileNotFoundError:
        print(f"Ошибка: не найден файл конфигурации {CONFIG_PATH}")
        return

    setup_logging(config["log_file"])
    logging.info("Программа запущена")

    input_path = BASE_DIR / config["input_file"]
    print("Файл с данными:", input_path)
    print("Файл существует:", input_path.exists())

    try:
        numbers = read_numbers(input_path)
        logging.info("Файл %s успешно прочитан", input_path.name)
        logging.info("Прочитано значений: %d", len(numbers))
        validate_numbers(numbers)
    except FileNotFoundError:
        logging.error("Файл не найден: %s", input_path)
        print("Ошибка: файл с измерениями не найден.")
    except ValueError as error:
        logging.error("Ошибка данных: %s", error)
        print("Ошибка данных:", error)
    else:
        print("Количество значений:", len(numbers))
        print("Минимум:", find_min(numbers))
        print("Максимум:", find_max(numbers))
        print("Среднее:", calculate_average(numbers))
        logging.info("Обработка данных завершена успешно")
    finally:
        logging.info("Программа завершена")


if __name__ == "__main__":
    main()
