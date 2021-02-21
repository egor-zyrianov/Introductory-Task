# -*- coding: utf-8 -*-
"""
Created on Thu Feb 11 23:45:48 2021

@author: B150M-C
"""

"""
Задача
На входе функция получает параметр n - 
натуральное число. Необходимо сгенерировать 
n-массивов, заполнить их случайными числами, 
каждый массив имеет случайный размер. 
Размеры массивов не должны совпадать. 
Далее необходимо отсортировать массивы. 
Массивы с четным порядковым номером 
отсортировать по возрастанию, 
с нечетным порядковым номером - 
по убыванию. На выходе функция должна 
вернуть массив с отсортированными массивами.
"""
#Seed for random()
try:
    from datetime import datetime
    t = datetime.now().microsecond / 1e6
except Exception:
    t = 0.5

"""
Логистическое отображение(имени Фейгенбаума) -
xn+1 = r*xn(1-xn) 
нелинейное уравнение с хаотическим поведением
начиная с r = 3.57
Аргументы:
    factor - множитель результата итерации
    subtrahend - сдвик влево результата итерации
return: число от 0 до 1 с вычетом 
    factor и множителем subtrahend
"""
xi = t
def random(factor = 1, subtrahend = 0):
    global xi
    r = 4 - 1e-5
    xn = r*xi*(1-xi)
    xi = xn
    return(round((xn-subtrahend) * factor, 3))
"""
Клвсс r-массива инициирующийся l = int, 
    length - длина = l
    data - лист случайных значений
order - возвращает длину r-массива
make - создает лист заданной длинны 
    заполненный r-массивами случайного размера
"""
class rarray():
    def __init__(self, l=0):
        self.length = l
        self.data = [random(2*l, 0.5) for count in range(self.length)]
        
    def order(a):
        return(a.length)
    
    def make(n):
        bucket = [0]*n
        for count in range(-1, n-1):
            bucket[count+1] = bucket[count] + int(random(n/1.1, -0.1)) 
        A = [rarray(x) for x in bucket]
        return(A)       
    
"""Тело алгоритма"""
def main(n):
    A = rarray.make(n) #инициация листа r-массивов
    
    A[::2] = sorted(A[::2], key=rarray.order) #сортировка четных элементов с нуливого
    A[1::2] = sorted(A[1::2], key=rarray.order, reverse=True) #обратная сортировка четных элементов с первого
    
    A = [a.data for a in A] #изъятие обработанных данных
    return(A)

print(main(10))
