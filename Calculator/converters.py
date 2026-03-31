def convert_temp(value, mode):
    if mode == "ctf":
        return f"Результат: {round(value * 1.8 + 32, 6)} F"
    elif mode == "ftc":
        return f"Результат: {round((value - 32) * 5 / 9, 6)} C"
    else:
        return "Операция не найдена"


def convert_dist(value, input_unit, output_unit):
    units = {
        "мм": 1,
        "см": 10,
        "дм": 100,
        "м": 1000,
        "км": 1000000
    }

    if input_unit not in units or output_unit not in units:
        return "Неизвестная единица"

    result = value * units[input_unit] / units[output_unit]
    return f"Результат: {round(result, 6)} {output_unit}"


def convert_speed(value, input_unit, output_unit):
    units = {
        "м/с": 1,
        "км/ч": 1 / 3.6
    }

    if input_unit not in units or output_unit not in units:
        return "Неизвестная единица"

    result = value * units[input_unit] / units[output_unit]
    return f"Результат: {round(result, 6)} {output_unit}"


def convert_volume(value, input_unit, output_unit):
    units = {
        "мл": 1,
        "см3": 1,
        "л": 1000,
        "м3": 1000000
    }

    if input_unit not in units or output_unit not in units:
        return "Неизвестная единица"

    result = value * units[input_unit] / units[output_unit]
    return f"Результат: {round(result, 6)} {output_unit}"


def convert_mass(value, input_unit, output_unit):
    units = {
        "мг": 1,
        "г": 1000,
        "кг": 1000000,
        "ц": 100000000,
        "т": 1000000000,
        "кт": 1000000000000,
        "мт": 1000000000000000
    }

    if input_unit not in units or output_unit not in units:
        return "Неизвестная единица"

    result = value * units[input_unit] / units[output_unit]
    return f"Результат: {round(result, 6)} {output_unit}"


def convert_area(value, input_unit, output_unit):
    units = {
        "мм2": 1,
        "см2": 100,
        "м2": 1000000,
        "км2": 1000000000000
    }

    if input_unit not in units or output_unit not in units:
        return "Неизвестная единица"

    result = value * units[input_unit] / units[output_unit]
    return f"Результат: {round(result, 6)} {output_unit}"