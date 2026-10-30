def read_numbers(file_path):

    numbers = []
    with open(file_path, "r", encoding="utf-8") as file:
        for line_number, line in enumerate(file, start=1):
            text = line.strip()
            if text == "":          # пустые строки пропускаем
                continue
            try:
                numbers.append(float(text))
            except ValueError:
                # Пробрасываем ту же ошибку, но с номером строки
                raise ValueError(
                    f"Некорректное значение в строке {line_number}: {text!r}"
                ) from None
    return numbers


def validate_numbers(numbers):
    if len(numbers) == 0:
        raise ValueError("Список измерений пуст")
