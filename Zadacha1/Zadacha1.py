# 1'. Вычислить число Пи c заданной точностью d
# *Пример:* 
# - при d = 0.001, π = 3.141
# - при d = 0.0001, π = 3.1415  
import math
def pi_res (n:float, d:float) -> float :
    d=str(d)
    d=len(d[d.find('.')+1::])
    stepper = 10.0 ** d
    #усечение
    a= math.trunc(stepper * n) / stepper
    return a
   
n=input('введите точность в формате "0.001":  ')
print(pi_res(math.pi, n))