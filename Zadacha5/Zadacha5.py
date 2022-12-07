# 5'. Даны два файла, в каждом из которых находится запись многочлена. Задача - сформировать файл, содержащий сумму многочленов.
# В file1.txt :
# 2*x**2 + 4*x + 5
# В file2.txt:
# 4*x**2 + 1*x + 4
# Результирующий файл:
# 6*x**2 + 5*x + 9
import sympy
from random import randint as rnd
def create_polinom(k: int, simple: bool = True) -> str:
    polinom = ''
    for i in range(k, -1, -1):
        polinom +=f'{rnd(0,2)}*x**{i}+'
        if i==0:
            polinom +=f'{rnd(0,100)}*x**{i}'
    if simple:
        return str(sympy.simplify(polinom))
    else:
        return str(polinom)
    
def create_pol_file(polinom: str, filename: str):
    with open(f'{filename}.txt', 'w') as f:
        f.write(polinom)

filename1 = 'first'
filename2 = 'second'
filename_sum = 'sum'
k=int(input('Задайте степень: '))
polinom1 = create_polinom(k)
polinom2 = create_polinom(k)
create_pol_file(polinom1, filename1)
create_pol_file(polinom2, filename2)

with open(f'{filename1}.txt', 'r') as f1:
        f_pol = f1.read()
        print(f'Первый полином  {f_pol}')
with open(f'{filename2}.txt', 'r') as f2:
        s_pol = f2.read()
        print(f'Второй полином  {s_pol}')
sum_pol = sympy.simplify(f_pol + '+' + s_pol)
sum_pol = str(sum_pol)
create_pol_file(sum_pol, filename_sum)