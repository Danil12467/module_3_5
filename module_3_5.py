def get_multiplied_digits(number):
    str_number = str(number)
    if len(str_number) == 1:
        return int(str_number)
    first = int(str_number[0])
    result = first * get_multiplied_digits(int(str_number[1:]))
    return result

result1 = get_multiplied_digits(40203)
print(result1)
result2 = get_multiplied_digits(203)
print(result2)