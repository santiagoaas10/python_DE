from functools import reduce


def calculate_average(numbers):
    if len(numbers) == 0:
        return 0
    sum_nums = reduce(lambda x, y: x + y, numbers)
    total = len(numbers)
    avg = sum_nums / total
    return avg
