def is_prime(func):
    def wrapper(*args, **kwargs):
        result_ = func(*args, **kwargs)
        summ = sum(args)
        j = 0
        for i in range(2, summ // 2 + 1):
            if summ % i == 0:
                j = j + 1
        if j <= 0:
            print('Простое')
        else:
            print('Составное')
        return result_
    return wrapper


@is_prime
def sum_three(*args):
    return sum(args)


result = sum_three(2, 3, 6)
print(result)
