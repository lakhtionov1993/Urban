numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
Primes = [] # список простых чисел
Not_Primes = [] # список не простых чисел
Primes_Not_Primes = [] # список делителей
for i in range(0, len(numbers)):
    for k in range(1, i+2):
        if k == i + 2:
            break
        elif numbers[i] % k == 0:
            Primes_Not_Primes.append(k)
            continue
    if len(Primes_Not_Primes) > 2:
        Not_Primes.append(numbers[i])
    elif len(Primes_Not_Primes) == 2:
        Primes.append(numbers[i])
    Primes_Not_Primes.clear()
    continue
print("Primes:", Primes, '''
''' "Not_Primes:", Not_Primes)




