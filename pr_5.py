#coding: utf-8
#Задача № 1
a = int (input ("Введите первое число: "))
b = int (input ("Введите второе число: "))
if a > b:
    print("Максимальное значение:", а)
else:
    print("Минимальное значение значение:", а)

#Задача № 2
c = int (input ("Введите сторону квадрата: "))
r = int (input ("Введите радиус круга: "))
d = (2 * c) ** 0.5
if d < 2 * r:
    print("круг")
     
#Задача № 3
c = int (input ("Введите число: "))
if x < 0:
    y = x ** 2
    print (y)
else:
    y = 1 / x ** 2
    
    print (y)
    
#Задача № 5
e = int (input ("Введите первое число: "))
f = int (input ("Введите второе число: "))
if e > f:
    print("Первое число больше второго") 
else:
    print("Второе число больше первого")