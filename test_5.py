def chain_sum_v1(chain_num=None):
    chain_sum = 0

    def sum(num=None):
        nonlocal chain_sum

        if num is None:
            return print(chain_sum)
        
        chain_sum += num
        return sum

    return sum(chain_num)

def chain_sum_v2(num=None, sum=0):
    if num is None:
        return print(sum)
    sum += num

    return lambda num=None, sum=sum: chain_sum_v2(num, sum)


#Tests
print("Вывод chain_sum_v1:")
chain_sum_v1()
chain_sum_v1(5)()
chain_sum_v1(5)(2)()
chain_sum_v1(5)(100)(-10)()
chain_sum_v1(5)(100)(-10)(900)()

print("Вывод chain_sum_v2:")
chain_sum_v2()
chain_sum_v2(5)()
chain_sum_v2(5)(2)()
chain_sum_v2(5)(100)(-10)()
chain_sum_v2(5)(100)(-10)(900)()