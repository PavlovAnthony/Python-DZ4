# 2'. Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.
# * 6 -> [1,2,3]
# * 144 -> [2,3]

def primfacs(num, unic:bool = False):
    i = 2
    primfac = []
    while num != 1 :
        while num % i == 0:
            primfac.append(i)
            num = num / i
        i = i + 1
    if unic:
        return list(set(primfac))
    else:
        return primfac
n = int(input('Задайте натуральное число : '))
print(f'Список уникальных делителей числа : {primfacs(n, True)}')
