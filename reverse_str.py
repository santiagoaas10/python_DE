def reverse_string(input_string):
    return input_string[::-1]


def reverse_string(input_string):
    limit = len(input_string)
    nueva_str = ""
    for i in range(limit - 1, -1, -1):
        nueva_str += input_string[i]
    return nueva_str
