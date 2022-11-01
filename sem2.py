# 1. Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
#  Пример:
# 6782 -> 23
# 0,56 -> 11


# number_str = input("Ввести число: ")
# sum = 0
# for digit_char in number_str:
#     if digit_char != ',':
#         digit = ord(digit_char) - ord('0')
#         sum = sum + digit
# print(sum) 


# 2. Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.

# Пример:
# пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

# array = []
# n = int(input("Ввести число: "))
# result = 1 
# for i in range(n):
#     result = result * (i+1)
#     array.append(result)
# print(*array)


# 3. Задайте список из n чисел последовательности (1+1/n)n и выведите на экран их сумму

#  Пример:
# Для n=4 {1: 2, 2: 2.25, 3: 2.37, 4: 2.44} 
# Сумма 9.06

# array = []
# n = int(input("Ввести число: "))
# sum = 0.0 
# for i in range(1, n+1):
#     result = (1.0 + 1.0/float(i))**i
#     result = round(result,2)
#     array.append(result)
#     sum = sum + result
# print(*array)
# print(sum)


# 4. Задайте список из N элементов, заполненных числами из промежутка [-N, N]. 
# Найдите произведение элементов на указанных позициях. 
# Позиции хранятся в файле file.txt в одной строке одно число.


# from random import randint

# def list(n):
#     list = []
#     for i in range(n):
#         list.append(randint(-n, n))
#     return list

# n = int(input('Введите число N: '))
# numbers = list(n)
# print(numbers)
# x = open('file.txt','r')
# result = numbers[int(x.readline())] * numbers[int(x.readline(2))]
# print(result)

#  5. Реализуйте алгоритм перемешивания списка.

# import random
# lst = [random.randint(0,10) for i in range(random.randint(5,20))]
# print(f"Какой-то список:\n {lst}")
# random.shuffle(lst)
# print(f"Он же после перемешивания:\n{lst}")