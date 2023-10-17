def get_duplicates(nums_list: list):
    unique_nums = set(nums_list)
    duplicates = list(num for num in unique_nums if nums_list.count(num) > 1)

    if len(duplicates) > 0:
        return print(sorted(duplicates))
    
    return print(None)

#tests
get_duplicates([1, 2, 3, 4, 3, 5, 6])
get_duplicates([81, 72, 43, 72, 81, 99, 99, 100, 12, 54])
get_duplicates([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
get_duplicates([91, 96, 60, 24, 96, 64, 88, 13, 19, 91])
get_duplicates([19, 25, 5, 31, 56, 36, 2, 35, 80, 26, 18, 60, 57, 17, 6, 18, 11, 89, 89, 55, 64, 75, 11, 69, 18, 79, 37, 6, 97, 27])
get_duplicates([60, 67, 41, 36, 61, 58, 42, 74, 71, 100, 8, 2, 40, 50, 28, 88, 35, 13, 66, 20, 4, 85, 62, 15, 80, 21, 81, 56, 77, 97])