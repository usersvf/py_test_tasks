import logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s, %(levelname)s, %(message)s'
)

import timeit

cache = {} #структура - {key= in функции : [val1= out функции, val2= количество вызовов с таким key]}

def cache_result(call_times=3):
    def execute_time(func):
        def wrapper(*args, **kwargs):
            start = timeit.default_timer()

            calls = [cnt[1] for cnt in cache.values()] #calls будет стартовать с нуля, т.к. изначально никаких значений нет -> calls = 0 первый вызов

            if sum(calls) > call_times - 1:
                cache.clear()

            if len(args) > 0:
                if cache.get(tuple(*args)) is None:
                    cache[tuple(*args)] = [func(*args, **kwargs), 1]
                else:
                    cache[tuple(*args)][1] += 1
            if len(kwargs) > 0:
                if cache.get(tuple(*[val for val in kwargs.values()])) is None:
                    cache[tuple(*[val for val in kwargs.values()])] = [func(*args, **kwargs), 1]
                else:
                    cache[tuple(*[val for val in kwargs.values()])][1] += 1

            end = timeit.default_timer()
            logging.info(f"Execute time {cache_result.__name__}: {(end - start) % 60:.7f} секунд")
        
        return wrapper
    
    return execute_time
    
#tests

@cache_result()
def get_duplicates(nums_list: list):
    unique_nums = set(nums_list)
    duplicates = list(num for num in unique_nums if nums_list.count(num) > 1)

    if len(duplicates) > 0:
        return sorted(duplicates)
    
    return print(None)

get_duplicates(nums_list=[1, 2, 3, 3])
print(cache)

get_duplicates([19, 4, 5, 31, 56, 36, 2, 35, 80, 26, 18, 60, 57, 17, 6, 18, 11, 89, 89, 55, 64, 75, 11, 69, 18, 79, 37, 6, 97, 27])
print(cache)

get_duplicates([19, 4, 5, 31, 56, 36, 2, 35, 80, 26, 18, 60, 57, 17, 6, 18, 11, 89, 89, 55, 64, 75, 11, 69, 18, 79, 37, 6, 97, 27])
print(cache)

get_duplicates([19, 25, 5, 31, 56, 36, 2, 35, 80, 26, 18, 60, 57, 17, 6, 18, 11, 89, 89, 55, 64, 75, 11, 69, 18, 79, 37, 6, 97, 27])
print(cache)