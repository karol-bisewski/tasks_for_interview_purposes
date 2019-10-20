def get_missing_numbers(input_list, n):
    return [x for x in range(1, n+1)
            if x not in input_list]


print(get_missing_numbers([2, 3, 7, 4, 9], 10))
