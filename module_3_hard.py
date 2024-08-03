def count_numbers_and_strings(data_structure):
    numbers = 0
    strings = 0

    def recurse(item):
        nonlocal numbers, strings
        if isinstance(item, (int, float)):
            numbers += 1
        elif isinstance(item, str):
            strings += 1
        elif isinstance(item, dict):
            for key, value in item.items():
                recurse(key)
                recurse(value)
        elif isinstance(item, (list, tuple, set)):
            for element in item:
                recurse(element)

    recurse(data_structure)
    return numbers, strings


data_structure = [[1, 2, 3], {'a': 4, 'b': 5}, (6, {'cube': 7, 'drum': 8}), "Hello",
                  ((), [{(2, 'Urban', ('Urban2', 35))}])]

numbers, strings = count_numbers_and_strings(data_structure)
print(f"Количество чисел: {numbers}")
print(f"Количество строк: {strings}")

