# №1 / 8 kyu / Reversed Strings

# Complete the solution so that it reverses the string passed into it.
#
# 'world'  =>  'dlrow'
# 'word'   =>  'drow'

# нужно конвертнуть слово, написать задам наперед
# def solution(string):
#     return ''.join(reversed(string))
#
# print(solution('world'))
# print(solution('word'))

# ----------------------------------------------------------------------------------------------------------------------#
# №2 / 8 kyu / Return Two Highest Values in List

# In this kata, your job is to return the two distinct highest values in a list. If there're less than 2 unique values,
# return as many of them, as possible.
#
# The result should also be ordered from highest to lowest.
#
# Examples:
#
# [4, 10, 10, 9]  =>  [10, 9]
# [1, 1, 1]  =>  [1]
# []  =>  []

# нужно найти два максимальных числа из списка
# def two_highest(lst):
#     if lst:
#         if set(lst) == {1}:
#             return lst[:1]
#         else:
#             unique = set(lst)
#             return sorted(list(unique), reverse=True)[:2]
#     else:
#         return lst
#
#
# print(two_highest([4, 10, 10, 9]))

# ----------------------------------------------------------------------------------------------------------------------#
# №3 / 8 kyu / Find Multiples of a Number

# In this simple exercise, you will build a program that takes a value, integer , and returns a list of its multiples up
# to another value, limit . If limit is a multiple of integer, it should be included as well. There will only ever be
# positive integers passed into the function, not consisting of 0. The limit will always be higher than the base.
#
# For example, if the parameters passed are (2, 6), the function should return [2, 4, 6] as 2, 4,
# and 6 are the multiples of 2 up to 6.

# нужно найти кратные числа для integer в заданном диапазоне (от integer до limit)
# def find_multiples(integer, limit):
#     return list(range(integer, limit + 1, integer))
#
#
# print(find_multiples(5, 25))

# ----------------------------------------------------------------------------------------------------------------------#
# №4 / 8 kyu / Beginner Series #1 School Paperwork

# Your classmates asked you to copy some paperwork for them. You know that there are 'n' classmates and the paperwork has 'm' pages.
#
# Your task is to calculate how many blank pages do you need. If n < 0 or m < 0 return 0.
#
# Example:
# n= 5, m=5: 25
# n=-5, m=5:  0
# Waiting for translations and Feedback! Thanks!

# простой выбор - либо то, либо то
# def paperwork(n, m):
#     return 0 if n < 0 or m < 0 else m * n

# второй варик
# def paperwork(n, m):
#     return (0, m * n)[m > 0 and n > 0]
#
#
# print(paperwork(55, 5))

# ----------------------------------------------------------------------------------------------------------------------#
# №5 / 8 kyu / Remove First and Last Character

# It('s pretty straightforward. Your goal is to create a function that removes the first and last characters of a string.'
#    'You')re given one parameter, the original string. You don't have to worry with strings with less than two characters

# задача убрать первый и последний символ строки
# def remove_char(s):
#     return s[1:-1] if len(s) > 2 else s

# 2
# def remove_char(s):
#     return (s, s[1:-1])[len(s) > 2]
#
#
# print(remove_char('ok'))

# ----------------------------------------------------------------------------------------------------------------------#
# №6 / 8 kyu / Is it even?

# In this Kata we are passing a number (n) into a function.
# Your code will determine if the number passed is even (or not).
# The function needs to return either a true or false.
# Numbers may be positive or negative, integers or floats.
# Floats with decimal part non equal to zero are considered UNeven for this kata.

# узнать четное честно или нет
# def is_even(n):
#     return bool(not(n % 2))
#
# print(is_even(-2))

# ----------------------------------------------------------------------------------------------------------------------#
# №7 / 8 kyu / Stringy Strings

# write me a function stringy that takes a size and returns a string of alternating 1s and 0s.
# the string should start with a 1.
# a string with size 6 should return :'101010'.
# with size 4 should return : '1010'.
# with size 12 should return : '101010101010'.
# The size will always be positive and will only use whole numbers.

# составить строку длинной size состоящую из чередующихся нулей и единиц
# def stringy(size):
#     s = '1'
#     for i in range(size - 1):
#         s += ('1', '0')[s[i] == '1']
#     return s
#
# print(stringy(5))

# 2
# def stringy(size):
#     return ('10' * size)[:size]

# ----------------------------------------------------------------------------------------------------------------------#
# №8 / 8 kyu / Find the smallest integer in the array

# Given an array of integers your solution should find the smallest integer.
#
# For example:
#
# Given [34, 15, 88, 2] your solution will return 2
# Given [34, -345, -1, 100] your solution will return -345
# You can assume, for the purpose of this kata, that the supplied array will not be empty.

# найти минимальное значение из списка
# def find_smallest_int(arr):
#     return min(arr)
#
# print(find_smallest_int([34, 15, 88, 2]))

# ----------------------------------------------------------------------------------------------------------------------#
# №9 / 8 kyu / Find the smallest integer in the array

# Given a string, you have to return a string in which each character (case-sensitive) is repeated once.
#
# Examples (Input -> Output):
# * "String"      -> "SSttrriinngg"
# * "Hello World" -> "HHeelllloo  WWoorrlldd"
# * "1234!_ "     -> "11223344!!__  "
# Good Luck!

# продублировать каждый элемент строки
# def double_char(s):
#     new_s = ''
#     for i in s:
#         new_s += i * 2
#     return new_s
#
# print(double_char('string'))

# 2
# def double_char(s):
#     return ''.join(i * 2 for i in s)
#
# print(double_char('sap'))

# ----------------------------------------------------------------------------------------------------------------------#
# 10 / 8 kyu / Name on billboard

# You can print your name on a billboard ad. Find out how much it will cost you. Each character has a default price of £30,
# but that can be different if you are given 2 parameters instead of 1 (allways 2 for Java).
# You can not use multiplier "*" operator.
# If your name would be Jeong-Ho Aristotelis, ad would cost £600. 20 leters * 30 = 600 (Space counts as a character).

# выполнить умножение без использования *
# def billboard(name, price=30):
#     l = len(name)
#     s = 0
#     return sum(s + price for i in range(l))
#
# # 2
# def billboard(name, price=30):
#     return sum(price for _ in name)
#
#
# print(billboard('Jeong-Ho Aristotelis'))

# ----------------------------------------------------------------------------------------------------------------------#
# 11 / 8 kyu / Incorrect division method

# This method, which is supposed to return the result of dividing its first argument by its second,
# isn't always returning correct values. Fix it.

# def divide_numbers(x, y):
#     return x / y
#
# print((divide_numbers(9, 4)))

# ----------------------------------------------------------------------------------------------------------------------#
# 12  8 kyu / Welcome to the City

# Create a method that takes as input a name, city, and state to welcome a person. Note that name will be an array
# consisting of one or more values that should be joined together with one space between each, and the length of the name array in test cases will vary.
#
# Example:
#
# ['John', 'Smith'], 'Phoenix', 'Arizona'
# This example will return the string Hello, John Smith! Welcome to Phoenix, Arizona!

# задача записать приветственную фразу. Тут прикольно, что имя и фамилия подается списком
# def say_hello(name, city, state):
#     s = ' '.join(i for i in name) # и мы ее тут преобразуем в строку
#     return f'Hello, {s}! Welcome to {city}, {state}!'
#
# print(say_hello(['John', 'Smith'], 'Phoenix', 'Arizona'))