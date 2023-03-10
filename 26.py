# Задача 26:  Напишите программу, которая на вход принимает два числа A и B, 
# и возводит число А в целую степень B с помощью рекурсии.

# *Пример:*

# A = 3; B = 5 -> 243 (3⁵)
#     A = 2; B = 3 -> 8 

# Рекурсия – это термин в программировании, означающий вызов функцией самой себя
# Опишем функцию, которая будет считать возведение в степень

def stepen_recurs(x, y):
    if (y == 1):
        return (x) #если степень равна 1, то функция возвращает изначальное число
    if (y != 1):
        return(x * stepen_recurs(x, y - 1))

a = int(input("Введите число А, которое будем возводить в степень: "))
b = int(input("Введите число В - степень, в которую возведем число А: "))
print(f"С помощью рекурсии возвезем число {a} в степень {b}")
print("Результат = : ", stepen_recurs(a, b))