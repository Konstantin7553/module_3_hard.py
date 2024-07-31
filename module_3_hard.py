def calculate_structure_sum(*args):
    num_count = 0
    str_count = 0

    for arg in args:
        if isinstance(arg, (int, float)):
            num_count += 1
        elif isinstance(arg, str):
            str_count += 1
        elif isinstance(arg, (list, tuple, set, dict)):
            if isinstance(arg, dict):
                sub_num, sub_str = calculate_structure_sum(*arg.keys(), *arg.values())
            else:
                sub_num, sub_str = calculate_structure_sum(*arg)
            num_count += sub_num
            str_count += sub_str

    return num_count, str_count

data_structure = [[1, 2, 3],{'a': 4, 'b': 5},(6, {'cube': 7, 'drum': 8}),"Hello",((),
[{(2, 'Urban', ('Urban2', 35))}])]
result = calculate_structure_sum(*data_structure)
print(result)
