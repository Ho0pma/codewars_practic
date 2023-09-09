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

# ----------------------------------------------------------------------------------------------------------------------#
# 13  8 kyu / Remove duplicates from list

# Define a function that removes duplicates from an array of non negative numbers and returns it as a result.
# The order of the sequence has to stay the same.
#
# Examples:
#
# Input -> Output
# [1, 1, 2] -> [1, 2]
# [1, 2, 1, 1, 3, 2] -> [1, 2, 3]

# Нужно убрать дубликаты и оставить порядок чисел таким же.
# def distinct(seq):
#     result_lst = []
#     for i in seq:
#         if i not in result_lst:
#             result_lst.append(i)
#     return result_lst

# 2 хороший варик, используем сет для удаления дубликатов и сортируем значения по индексам из поступающего списка seq
# def distinct(seq):
#     return sorted(set(seq), key=seq.index)

# 3 можно добиться удаления дубликатов путем создания словаря. fromkeys - создаст словарь и поставит для всех уникальных
# значений списка дефолтное значение - 0. Точно также можно решить через OrderedDict
# def distinct(seq):
#     return list(dict.fromkeys(seq))
#
# print(distinct([1, 2, 1, 1, 3, 2]))

# ----------------------------------------------------------------------------------------------------------------------#
# 14  7 kyu / Remove duplicate words

# Your task is to remove all duplicate words from a string, leaving only single (first) words entries.
#
# Example:
# Input:
# 'alpha beta beta gamma gamma gamma delta alpha beta beta gamma gamma gamma delta'
#
# Output:
# 'alpha beta gamma delta'

# задача вернуть только уникальные слова из строки
# def remove_duplicate_words(s):
#     lst = s.split()
#     return ' '.join(sorted(set(lst), key=lst.index))
#
# print(remove_duplicate_words('alpha beta beta gamma gamma gamma delta alpha beta beta gamma gamma gamma delta'))

# ----------------------------------------------------------------------------------------------------------------------#
# 14  7 kyu / Simple remove duplicates

# Remove the duplicates from a list of integers, keeping the last ( rightmost ) occurrence of each element.
#
# Example:
# For input: [3, 4, 4, 3, 6, 3]
#
# remove the 3 at index 0
# remove the 4 at index 1
# remove the 3 at index 3
# Expected output: [4, 6, 3]

# задача вывести только уникальные интовые значения, сохраняя при этом порядок. Нужно чтобы в список добавлялась только
# последнее значение
# def solve(arr):
#     lst = []
#     for i in reversed(arr):
#         if i not in lst:
#             lst.append(i)
#
#     lst.reverse()
#     return lst
#
# print(solve([1,2,1,2,1,2,3]))

# 2
# def solve(arr):
#     return list(dict.fromkeys(arr[::-1]))[::-1]
#
# print(solve([1, 2, 1, 2, 1, 2, 3]))

# ----------------------------------------------------------------------------------------------------------------------#
# 15  7 kyu / Remove consecutive duplicate words

# Your task is to remove all consecutive duplicate words from a string, leaving only first words entries. For example:
#
# "alpha beta beta gamma gamma gamma delta alpha beta beta gamma gamma gamma delta"
#
# --> "alpha beta gamma delta alpha beta gamma delta"
# Words will be separated by a single space. There will be no leading or trailing spaces in the string. An empty string
# (0 words) is a valid input.

# задача убрать повторяющиеся элементы (идущие друг за другом)
# def remove_consecutive_duplicates(s: str) -> str:
#     lst = s.split()
#     new_lst = []
#     for i in range(len(lst)):
#         if i != len(lst) - 1:
#             if lst[i] == lst[i + 1]:
#                 continue
#             else:
#                 new_lst.append(lst[i])
#         else:
#             new_lst.append(lst[i])
#     return ' '.join(new_lst)

# 2
# from itertools import groupby
# def remove_consecutive_duplicates(s: str) -> str:
#     return ' '.join(k for k, _ in groupby(s.split()))
#
# print(remove_consecutive_duplicates('alpha beta beta gamma gamma gamma delta alpha beta beta gamma gamma gamma delta'))


# пример работы groupby (если последовательность отсортирована - выдаст (значение, кол-во вхождений)
# если не отсортирована как в примере ниже, то сгруппирует последовательно. В итоге будет две 4ки
# будет (значение = 4: кол-во = 1) и потом еще раз (значение = 4: кол-во = 2)
# from itertools import groupby
# sequence = [1, 1, 2, 2, 3, 3, 3, 4, 5, 4, 4] # Исходная последовательность
# grouped = groupby(sequence) # Группировка элементов по их значениям
#
# # Проход по группам и вывод результатов
# for key, group in grouped:
#     print(f"Значение {key} встречается {len(list(group))} раз(а)")

# ----------------------------------------------------------------------------------------------------------------------#
# 16  8 kyu / Remove First and Last Character Part Two

# This is a spin off of my first kata.
#
# You are given a string containing a sequence of character sequences separated by commas.
# Write a function which returns a new string containing the same character sequences except the first and the last
# ones but this time separated by spaces.
# If the input string is empty or the removal of the first and last items would cause the resulting string to be empty,
# return an empty value (represented as a generic value NULL in the examples below).
#
# Examples
# "1,2,3"      =>  "2"
# "1,2,3,4"    =>  "2 3"
# "1,2,3,4,5"  =>  "2 3 4"
#
# ""     =>  NULL
# "1"    =>  NULL
# "1,2"  =>  NULL

# задача: нужно убрать из строки первый и последний элемент
# def array(string):
#     lst = string.split(',')[1:-1]
#     return (None, ' '.join(lst))[len(lst) >= 1]

# 2 прикольно что если сравнивает пустое или не пустое
# def array(string):
#     return ' '.join(string.split(','))[1:-1] or None
#
# print(array('1,2,3,4,5'))

# ----------------------------------------------------------------------------------------------------------------------#
# 17  7 kyu / Remove Unnecessary Characters from Items in List

# You('ve been given a list that states the daily revenue for each day of the week. Unfortunately, '
#     'the list has been corrupted and contains extraneous characters. Rather than fix the source of the problem, '
#     'your boss has asked you to create a program that removes any unneccessary characters and return the corrected list.)
#
# The expected characters are digits, ' $ ', and ' . ' All items in the returned list are expected to be strings.
#
# For example:
#
# a1 = ['$5.$6.6x.s4', '{$33ae.5(9', '$29..4e9', '%.$9|4d20', 'A$AA$4r R4.94']
# remove_char(a1)
# >>> ['$56.64', '$33.59', '$29.49', '$94.20', '$44.94']

# import re
# def remove_char(array):
#     res_lst = []
#     for i in array:
#         output_string = re.sub(r'[^0-9]', '', i)
#         if len(output_string) == 4:
#             output_string = f'${output_string[:2]}.{output_string[2:]}'
#         else:
#             output_string = f'${output_string[:1]}.{output_string[2:]}'
#
#         res_lst.append(output_string)
#
#     return res_lst
#
#
# print(remove_char(['$5.$6.6x.s4', '{$33ae.5(9', '$29..4e9', '%.$9|4d20', 'A$AA$4r R4.94']))

# ----------------------------------------------------------------------------------------------------------------------#
# ARRAYS

# 19  8 kyu / Printing Array elements with Comma delimiters

# Input: Array of elements
# ["h","o","l","a"]
#
# Output: String with comma delimited elements of the array in th same order.
# "h,o,l,a"
#
# Note: if this seems too simple for you try the next level

# def print_array(arr):
#     seq = ''
#     for i in arr:
#         seq += f'{str(i)} '
#     return seq.replace(' ', ',')[:-1]
#
# print(print_array(["2","4","5","2"]))

# 2
# def print_array(arr):
#     return ', '.join(str(i) for i in arr)
#
# print(print_array(["2","4","5","2"]))

# ----------------------------------------------------------------------------------------------------------------------#
# 20  8 kyu / Removing Elements

# Take an array and remove every second element from the array.
# Always keep the first element and start removing with the next element.
#
# Example:
# ["Keep", "Remove", "Keep", "Remove", "Keep", ...] --> ["Keep", "Keep", "Keep", ...]
#
# None of the arrays will be empty, so you don't have to worry about that!

# задача вывести элемента массива через 1
# def remove_every_other(my_list):
#     return my_list[::2]
#
# print(remove_every_other(["Keep", "Remove", "Keep", "Remove", "Keep"]))

# ----------------------------------------------------------------------------------------------------------------------#
# 21  8 kyu / Removing Elements

# def flip(d, a):
#     return sorted(a) if d == 'R' else sorted(a, reverse=True)

# 2
# def flip(d, a):
#     return sorted(a, reverse=True == 'L') # условие сортировки
#
# print(flip('R', [3, 2, 1, 2]))
# print(flip('L', [1, 4, 5, 3, 5 ]))

# ----------------------------------------------------------------------------------------------------------------------#
# 22  8 kyu / Calculate average

# Write a function which calculates the average of the numbers in a given list.
# Note: Empty arrays should return 0.

# задача найти среднее значение списка
# def find_average(numbers):
#     return sum(numbers) / len(numbers) if numbers else 0
#
#
# print(find_average([]))

# ----------------------------------------------------------------------------------------------------------------------#
# 23  8 kyu / Fake Binary

# Given a string of digits, you should replace any digit below 5 with '0' and any digit 5 and above with '1'.
# Return the resulting string.
# Note: input will never be an empty string

# задача заменить цифры на 1 и 0 (если меньше 5 - 0, больше - 1)
# def fake_bin(x):
#     new_s = ''
#     for i in x:
#         if int(i) >= 5:
#             new_s += '1'
#         else:
#             new_s += '0'
#
#     return new_s

# 2 использование генератора
# def fake_bin(x):
#     return ''.join('0' if i < '5' else '1' for i in x)
#
#
# print(fake_bin("45385593107843568"))

# ----------------------------------------------------------------------------------------------------------------------#
# 24  8 kyu / Convert a string to an array

# Write a function to split a string and convert it into an array of words.
#
# Examples (Input ==> Output):
# "Robin Singh" ==> ["Robin", "Singh"]
#
# "I love arrays they are my favorite" ==> ["I", "love", "arrays", "they", "are", "my", "favorite"]

# задача разбить строку на список из строк
# def string_to_array(s):
#     return s.split() if s else ['']


# 2 тут прикольно, что если первое пустое - выберется второе
# def string_to_array(s):
#     return s.split() or ['']
# print(string_to_array("Robin Singh"))

# ----------------------------------------------------------------------------------------------------------------------#
# 25  8 kyu / A Needle in the Haystack

# Can you find the needle in the haystack?
#
# Write a function findNeedle() that takes an array full of junk but containing one "needle"
#
# After your function finds the needle it should return a message (as a string) that says:
#
# "found the needle at position " plus the index it found the needle, so:
#
# Example(Input --> Output)
#
# ["hay", "junk", "hay", "hay", "moreJunk", "needle", "randomJunk"] --> "found the needle at position 5"
# Note: In COBOL, it should return "found the needle at position 6"

# задача вернуть индекс значения, которое мы ищем (needle)
# def find_needle(haystack):
#     return f'found the needle at position {haystack.index("needle")}'
#
#
# print(find_needle(["hay", "junk", "hay", "hay", "moreJunk", "needle", "randomJunk"]))

# ----------------------------------------------------------------------------------------------------------------------#
# 26  8 kyu / Sentence Smash

# Sentence Smash
# Write a function that takes an array of words and smashes them together into a sentence and returns the sentence.
# You can ignore any need to sanitize words or add punctuation, but you should add spaces between each word. Be careful,
# there shouldn't be a space at the beginning or the end of the sentence!
#
# Example
# ['hello', 'world', 'this', 'is', 'great']  =>  'hello world this is great'

# задача преобразовать список в строку
# def smash(words):
#     return ' '.join(words)
#
# print(smash(['hello', 'world', 'this', 'is', 'great']))

# ----------------------------------------------------------------------------------------------------------------------#
# 27  8 kyu / Multiple of index

# Return a new array consisting of elements which are multiple of their own index in input array (length > 1).
#
# Some cases:
# [22, -6, 32, 82, 9, 25] =>  [-6, 32, 25]
#
# [68, -1, 1, -7, 10, 10] => [-1, 10]
#
# [-56,-85,72,-26,-14,76,-27,72,35,-21,-67,87,0,21,59,27,-92,68] => [-85, 72, 0, 68]

# задача добавить в новый список значения только кратные индексу
# def multiple_of_index(arr):
#     new_arr = []
#     for index, value in enumerate(arr):
#         if index == 0 and value != 0:
#             continue
#         if value != 0:
#             if value % index == 0:
#                 new_arr.append(value)
#         else:
#             new_arr.append(value)
#     return new_arr
#
#
# print(multiple_of_index([0, 71, 44, -44]))

# ----------------------------------------------------------------------------------------------------------------------#
# 28  8 kyu / Sort and Star

# You will be given a list of strings. You must sort it alphabetically
# (case-sensitive, and based on the ASCII values of the chars) and then return the first value.
#
# The returned value must be a string, and have "***" between each of its letters.
#
# You should not remove or add elements from/to the array.

# задача сделать сортировку и вернуть первое слово в таком стиле: b***i***t***c***o***i***n
# def two_sort(array):
#     return '***'.join(sorted(array)[0])
#
# print(two_sort(["bitcoin", "take", "over", "the", "world", "maybe", "who", "knows", "perhaps"]))

# ----------------------------------------------------------------------------------------------------------------------#
# 29  8 kyu / Array plus array

# I('m new to coding and now I want to get the sum of two arrays... '
#   'Actually the sum of all their elements. I')ll appreciate for your help.
#
# P.S. Each array includes only integer numbers. Output is a number too.

# задача вернуть общую сумму списков
# def array_plus_array(arr1, arr2):
#     return sum(arr1 + arr2)
#
# print(array_plus_array([1, 2, 3], [4, 5, 6]))

# ----------------------------------------------------------------------------------------------------------------------#
# 30  8 kyu / Total amount of points

# Our football team has finished the championship.
#
# Our team('s match results are recorded in a collection of strings. Each match is represented '
#          'by a string in the format "x:y", where x is our team')s score and y is our opponents score.
#
# For example: ["3:1", "2:2", "0:1", ...]
#
# Points are awarded for each match as follows:
#
# if x > y: 3 points (win)
# if x < y: 0 points (loss)
# if x = y: 1 point (tie)
# We need to write a function that takes this collection and returns the number of points our team (x)
# got in the championship by the rules given above.
#
# Notes:
#
# our team always plays 10 matches in the championship
# 0 <= x <= 4
# 0 <= y <= 4

# задача посчитать кол-во очков за чемпионат. +3 за победу, 1 за ничью, 0 за проеб
# def points(games):
#     total_value = 0
#     for i in games:
#         if i[0] > i[2]:
#             total_value += 3
#         elif i[0] == i[2]:
#             total_value += 1
#     return total_value
#
# print(points(['1:0', '2:0', '3:0', '4:0', '2:1', '3:1', '4:1', '3:2', '4:2', '4:3']))

# ----------------------------------------------------------------------------------------------------------------------#
# 31  8 kyu / Convert number to reversed array of digits

# Convert number to reversed array of digits
# Given a random non-negative number, you have to return the digits of this number within an array in reverse order.
#
# Example(Input => Output):
# 35231 => [1,3,2,5,3]
# 0 => [0]

# задача из введенного числа получить список чисел составляющих это число
# def digitize(n):
#     return [int(i) for i in list(str(n))[::-1]]
#
#
# print(digitize(35231))

# ----------------------------------------------------------------------------------------------------------------------#
# 32  8 kyu / Sum of positive
#
# You get an array of numbers, return the sum of all of the positives ones.
#
# Example [1,-4,7,12] => 1 + 7 + 12 = 20
#
# Note: if there is nothing to sum, the sum is default to 0.

# вернуть сумму только положительных чисел в списке
# def positive_sum(arr):
#     return sum([i for i in arr if i > 0])

# 2 можно без лист компр, через генератор
# def positive_sum(arr):
#     return sum(i for i in arr if i > 0)
# print(positive_sum([1, -4, 7, 12]))

# ----------------------------------------------------------------------------------------------------------------------#
# 33  8 kyu / Get the mean of an array

# It's the academic year's end, fateful moment of your school report. The averages must be calculated.
# All the students come to you and entreat you to calculate their average for them. Easy ! You just need to write a script.
#
# Return the average of the given array rounded down to its nearest integer.
#
# The array will never be empty.

# задача посчитать среднее от списка и округлить в меньшую строну
# from math import floor
# def get_average(marks):
#     return floor(sum(marks) / len(marks))
#
# print(get_average([1, 5, 87, 45, 8, 8]))

# 2 без импортов, это же просто целочисленное деление
# def get_average(marks):
#     return sum(marks) // len(marks)
#
# print(get_average([2, 2, 2, 2]))

# ----------------------------------------------------------------------------------------------------------------------#
# 34  8 kyu / Beginner - Reduce but Grow

# Given a non-empty array of integers, return the result of multiplying the values together in order. Example:
#
# [1, 2, 3, 4] => 1 * 2 * 3 * 4 = 24

# задача перемножить все числа в списке
# def grow(arr):
#     return eval(str(arr)[1:-1].replace(', ', '*'))

# есть еще вариант через math, тоже перемножает элементы массива
# def grow(arr):
#     return __import__('math').prod(arr)
#
# print(grow([1, 2, 3, 4]))

# ----------------------------------------------------------------------------------------------------------------------#
# 35  8 kyu / Invert values

# Given a set of numbers, return the additive inverse of each. Each positive becomes negatives,
# and the negatives become positives.
#
# invert([1,2,3,4,5]) == [-1,-2,-3,-4,-5]
# invert([1,-2,3,-4,5]) == [-1,2,-3,4,-5]
# invert([]) == []
# You can assume that all values are integers. Do not mutate the input array/list.

# задача изменить знак числа в списке
# def invert(lst):
#     return [-1 * i for i in lst]

# 2 можно не умножать, а просто написать -i
# def invert(lst):
#     return [-i for i in lst]
#
# print(invert([1, 2, 3, 4, -5]))

# ----------------------------------------------------------------------------------------------------------------------#
# 36  8 kyu / My head is at the wrong end!

# You('re at the zoo... all the meerkats look weird. '
#     'Something has gone terribly wrong - someone has gone and switched their heads and tails around!)
#
# Save the animals by switching them back. You will be given an array which will have three values
# (tail, body, head). It is your job to re-arrange the array so that the animal is the right way round (head, body, tail).
#
# Same goes for all the other arrays/lists that you will get in the tests:
#     you have to change the element positions with the same exact logics
#
# Simples!

# задача хуита, нужно просто перевернуть массив
# def fix_the_meerkat(arr):
#     return arr[::-1]
#
# print(fix_the_meerkat(["tail", "body", "head"]))

# ----------------------------------------------------------------------------------------------------------------------#
# 37  8 kyu / Filter out the geese
#
# Write a function that takes a list of strings as an argument and returns a filtered list containing
# the same elements but with the 'geese' removed.
# The geese are any strings in the following array, which is pre-populated in your solution:
#
#   ["African", "Roman Tufted", "Toulouse", "Pilgrim", "Steinbacher"]
# For example, if this array were passed as an argument:
#
#  ["Mallard", "Hook Bill", "African", "Crested", "Pilgrim", "Toulouse", "Blue Swedish"]
# Your function would return the following array:
#
# ["Mallard", "Hook Bill", "Crested", "Blue Swedish"]
# The elements in the returned array should be in the same order as in the initial array passed to your function, albeit
# with the 'geese' removed. Note that all of the strings will be in the same case as those provided, and some elements may be repeated.

# задача отрефакторить поступающий список. Вывести только те элементы списка, которых нет в geese
# geese = ["African", "Roman Tufted", "Toulouse", "Pilgrim", "Steinbacher"]
# def goose_filter(birds):
#     return [i for i in birds if i not in geese]
#
# print(goose_filter(["Mallard", "Hook Bill", "African", "Crested", "Pilgrim", "Toulouse", "Blue Swedish"]))

# ----------------------------------------------------------------------------------------------------------------------#
# 38  8 kyu / Is there a vowel in there?

# Given an array of numbers, check if any of the numbers are the character codes for lower case vowels (a, e, i, o, u).
# If they are, change the array value to a string of that vowel.
# Return the resulting array.

# задача: заменить число на его chr значение, если оно входит в (a, e, i, o, u)
# def is_vow(inp):
#     return [chr(i) if i in {97, 111, 101, 117, 105} else i for i in inp]
#
# print(is_vow([118, 117, 120, 121, 117, 98, 122, 97, 120, 106, 104, 116, 113, 114, 113, 120, 106]))

# ----------------------------------------------------------------------------------------------------------------------#
# 39  8 kyu / Count the Monkeys!

# You take your son to the forest to see the monkeys. You know that there are a certain number there (n),
# but your son is too young to just appreciate the full number, he has to start counting them from 1.
#
# As a good parent, you will sit and count with him. Given the number (n), populate an array with all
# numbers up to and including that number, but excluding zero.
#
# For example(Input --> Output):
#
# 10 --> [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#  1 --> [1]

# задача создать список из возрастающих чисел. Длина передается в качестве аргумента
# def monkey_count(n):
#     return [i + 1 for i in range(n)]
#
# print(monkey_count(10))

# ----------------------------------------------------------------------------------------------------------------------#
# 40  8 kyu / Beginner - Lost Without a Map

# Given an array of integers, return a new array with each value doubled.
#
# For example:
#
# [1, 2, 3] --> [2, 4, 6]

# вернуть х2 значение из списка
# def maps(a):
# return [i * 2 for i in a]

# 2 через лямбду + map
# def maps(a):
#     return list(map(lambda x: x * 2, a))
#
# print(maps([1, 2, 3]))

# ----------------------------------------------------------------------------------------------------------------------#
# 41  8 kyu / No Loops 2 - You only need one
#
# *** No Loops Allowed ***
#
# You will be given an array a and a value x. All you need to do is check whether the provided array contains the value, without using a loop.
#
# Array can contain numbers or strings. x can be either. Return true if the array contains the value, false if not.
# With strings you will need to account for case.
#
# Looking for more, loop-restrained fun? Check out the other kata in the series:
#
# No Loops 1 - Small enough?

# задача проверить есть ли x в a
# def check(a, x):
#     return x in a
#
# print(check(['what', 'a', 'great', 'kata'], 'kat'))

# ----------------------------------------------------------------------------------------------------------------------#
# 42  8 kyu / No Loops 2 - You only need one

# Write a function that takes an array of numbers and returns the sum of the numbers.
# The numbers can be negative or non-integer. If the array does not contain any numbers then you should return 0.
#
# Examples
# Input: [1, 5.2, 4, 0, -1]
# Output: 9.2
#
# Input: []
# Output: 0
#
# Input: [-2.398]
# Output: -2.398
#
# Assumptions
# You can assume that you are only given numbers.
# You cannot assume the size of the array.
# You can assume that you do get an array and if the array is empty, return 0.
# What We're Testing
# We're testing basic loops and math operations. This is for beginners who are just learning loops and math operations.
# Advanced users may find this extremely easy and can easily write this in one line.

# задача просуммировать числа в массиве
# def sum_array(a):
#     return sum(a)
#
# print(sum_array([1, 2, 3]))
# print(sum_array([]))

# ----------------------------------------------------------------------------------------------------------------------#
# 43  8 kyu / No Loops 2 - You only need one

# Who remembers back to their time in the schoolyard, when girls would take a flower and
# tear its petals, saying each of the following phrases each time a petal was torn:
#
# "I love you"
# "a little"
# "a lot"
# "passionately"
# "madly"
# "not at all"
# If there are more than 6 petals, you start over with "I love you" for 7 petals, "a little" for 8 petals and so on.
#
# When the last petal was torn there were cries of excitement, dreams, surging thoughts and emotions.
#
# Your goal in this kata is to determine which phrase the girls would say at the last petal for
#     a flower of a given number of petals. The number of petals is always greater than 0.

# задача вывести значение по ключу из словаря, если аргумент > существующих ключей - идти по кругу
# def how_much_i_love_you(nb_petals):
#     d = {
#         1: "I love you",
#         2: "a little",
#         3: "a lot",
#         4: "passionately",
#         5: "madly",
#         6: "not at all"
#     }
#     mod = nb_petals % 6
#     return d[mod] if mod != 0 else d[6]
#
# print(how_much_i_love_you(6))

# ----------------------------------------------------------------------------------------------------------------------#
# 44  8 kyu / Find the first non-consecutive number

# Your task is to find the first element of an array that is not consecutive.
# By not consecutive we mean not exactly 1 larger than the previous element of the array.
# E.g. If we have an array [1,2,3,4,6,7,8] then 1 then 2 then 3 then 4 are all consecutive but 6 is not,
# so that's the first non-consecutive number.
# If the whole array is consecutive then return null2.
# The array will always have at least 2 elements1 and all elements will be numbers. The numbers will also all be unique
# and in ascending order. The numbers could be positive or negative and the first non-consecutive could be either too!

# задача: нужно найти момент когда нарушена последовательность
# def first_non_consecutive(arr):
#     for i in range(1, len(arr)):
#         a = arr[i]
#         b = arr[i - 1]
#         if arr[i] == arr[i - 1] + 1:
#             continue
#         else:
#             return arr[i]
#
# 2 варик через enumerate
# def first_non_consecutive(arr):
#     for i, v in enumerate(arr, arr[0]):
#         if v != i: return v
#
# print(first_non_consecutive([1, 2, 3, 4, 6, 7]))

# ----------------------------------------------------------------------------------------------------------------------#
# 45  8 kyu / To square(root) or not to square(root)
#
# Write a method, that will get an integer array as parameter and will process every number from this array.
#
# Return a new array with processing every number of the input-array like this:
#
# If the number has an integer square root, take this, otherwise square the number.
#
# Example
# [4,3,9,7,2,1] -> [2,9,3,49,4,1]
# Notes
# The input array will always contain only positive numbers, and will never be empty or null.

# задача: нужно возвести в квадрат те числа, от которых нельзя взять чистый корень.
# def square_or_square_root(arr):
#     new_arr = []
#     for i in arr:
#         square = __import__('math').sqrt(i)
#         if str(square)[-1] == '0':
#             new_arr.append(round(square))
#         else:
#             new_arr.append(i**2)
#     return new_arr

# 2 Остаток от деления!
# from math import sqrt
# def square_or_square_root(arr):
#     return [int(sqrt(i)) if sqrt(i) % 1 == 0 else i ** 2 for i in arr]
#
#
# print(square_or_square_root([4, 3, 9, 7, 2, 1]))

# ----------------------------------------------------------------------------------------------------------------------#
# 46  8 kyu / Count by X

# Create a function with two arguments that will return an array of the first n multiples of x.
#
# Assume both the given number and the number of times to count will be positive numbers greater than 0.
#
# Return the results as an array or list ( depending on language ).
#
# Examples
# count_by(1,10) #should return [1,2,3,4,5,6,7,8,9,10]
# count_by(2,5) #should return [2,4,6,8,10]

# задача: вывести кратные Х числа, на диапазоне x * n
# def count_by(x, n):
#     return [i for i in range(1, x*n + 1) if i % x == 0]

# 2 это тоже самое если умножать ...
# def count_by(x, n):
#     return [i * x for i in range(1, n + 1)]

# print(count_by(3, 5))

# ----------------------------------------------------------------------------------------------------------------------#
# 47  8 kyu / Find numbers which are divisible by given number

# Complete the function which takes two arguments and returns all numbers which are divisible by the given divisor.
# First argument is an array of numbers and the second is the divisor.
#
# Example(Input1, Input2 --> Output)
# [1, 2, 3, 4, 5, 6], 2 --> [2, 4, 6]

# задача вернуть массив чисел, которые кратны divisor
# def divisible_by(numbers, divisor):
#     return [i for i in numbers if i % divisor == 0]
#
# print(divisible_by([1, 2, 3, 4, 5, 6], 2))

# ----------------------------------------------------------------------------------------------------------------------#
# 48  8 kyu / Sum Mixed Array

# Given an array of integers as strings and numbers, return the sum of the array values as if all were numbers.
#
# Return your answer as a number.

# вернуть сумму списка
# def sum_mix(arr):
#     return sum([int(i) for i in arr])
#
# print(sum_mix([9, 3, '7', '3']))

# ----------------------------------------------------------------------------------------------------------------------#
# 49  8 kyu / ???

# You are given two sorted arrays that both only contain integers. Your task is to find a way to merge them
# into a single one, sorted in asc order. Complete the function mergeArrays(arr1, arr2),
# where arr1 and arr2 are the original sorted arrays.
# You don('t need to worry about validation, since arr1 and arr2 must be arrays with 0 or more Integers. '
#         'If both arr1 and arr2 are empty, then just return an empty array.)
#
# Note: arr1 and arr2 may be sorted in different orders. Also arr1 and arr2 may have same integers.
# Remove duplicated in the returned result.

# Examples (input -> output)
# * [1, 2, 3, 4, 5], [6, 7, 8, 9, 10] -> [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# * [1, 3, 5, 7, 9], [10, 8, 6, 4, 2] -> [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# * [1, 3, 5, 7, 9, 11, 12], [1, 2, 3, 4, 5, 10, 12] -> [1, 2, 3, 4, 5, 7, 9, 10, 11, 12]

# задача соединить два массива и получить список уникальных чисел
# def merge_arrays(arr1, arr2):
#     return sorted(set(arr1 + arr2))
#
# print(merge_arrays([1, 2, 3, 4, 5], [6, 7, 8, 9, 10]))

# ----------------------------------------------------------------------------------------------------------------------#
# 50  8 kyu / Well of Ideas - Easy Version

# For every good kata idea there seem to be quite a few bad ones!
#
# In this kata you need to check the provided array (x) for good ideas 'good' and bad ideas 'bad'. If there are one
# or two good ideas, return 'Publish!', if there are more than 2 return
# 'I smell a series!'. If there are no good ideas, as is often the case, return 'Fail!'.

# задача на подсчет элементов в списке.
# from collections import Counter
# def well(x):
#     d = Counter(x)
#     if 1 <= d['good'] <= 2:
#         return 'Publish!'
#     elif d['good'] > 2:
#         return 'I smell a series!'
#     else:
#         return 'Fail!'
#
# print(well(['good', 'bad', 'bad', 'bad', 'bad']))

# ----------------------------------------------------------------------------------------------------------------------#
# 51  8 kyu / A wolf in sheep's clothing

# Wolves have been reintroduced to Great Britain. You are a sheep farmer, and
# are now plagued by wolves which pretend to be sheep. Fortunately, you are good at spotting them.
#
# Warn the sheep in front of the wolf that it is about to be eaten.
# Remember that you are standing at the front of the queue which is at the end of the array:
#
# [sheep, sheep, sheep, sheep, sheep, wolf, sheep, sheep]      (YOU ARE HERE AT THE FRONT OF THE QUEUE)
#    7      6      5      4      3            2      1
# If the wolf is the closest animal to you, return "Pls go away and stop eating my sheep".
# Otherwise, return "Oi! Sheep number N! You are about to be eaten by a wolf!" where N is the sheep's position in the queue.
#
# Note: there will always be exactly one wolf in the array.
#
# Examples
# Input: ["sheep", "sheep", "sheep", "wolf", "sheep"]
# Output: "Oi! Sheep number 1! You are about to be eaten by a wolf!"
#
# Input: ["sheep", "sheep", "wolf"]
# Output: "Pls go away and stop eating my sheep"

# задача на поиск элемента в списке через индекс
# def warn_the_sheep(queue):
#     position = len(queue) - queue.index('wolf')
#     return (f"Oi! Sheep number {position - 1}! You are about to be eaten by a wolf!", "Pls go away and stop eating my sheep")[position == 1]
#
# print(warn_the_sheep(["sheep", "sheep", "sheep", "sheep", "wolf"]))

# ----------------------------------------------------------------------------------------------------------------------#
# 53  8 kyu /

# задача о сумме списков в списке
# s = [[1, 2, 3], [4, 5, 6]]
# total_sum = 0
# for i in s:
#     total_sum += sum(i)
# print(total_sum)

# ----------------------------------------------------------------------------------------------------------------------#
# 53  8 kyu / Enumerable Magic #20 - Cascading Subsets
# Create a method each_cons that accepts a list and a number n, and returns cascading subsets of the list of size n, like so:
# each_cons([1, 2, 3, 4], 2)
# # => [[1,2], [2,3], [3,4]]
#
# each_cons([1, 2, 3, 4], 3)
# # => [[1,2,3],[2,3,4]]

# задача (сложно) создать списки в списке по аналогии сверху
# def each_cons(lst, n):
#     lst_for_zip = []
#     for i in range(n):
#         lst_for_zip.append(lst[i:])
#
#     return [list(i) for i in zip(*lst_for_zip)]
#
# 2
# def each_cons(lst, n):
#     return [lst[i:i + n] for i in range(len(lst) - n + 1)]
# print(each_cons([3, 5, 8, 13], 3))

# ----------------------------------------------------------------------------------------------------------------------#
# 54  8 kyu / Enumerable Magic #1 - True for All?

# Task
# Create a method all which takes two params:
#
# a sequence
# a function (function pointer in C)
# and returns true if the function in the params returns true for every element
#     in the sequence. Otherwise, it should return false. If the sequence is empty,
#     it should return true, since technically nothing failed the test.
#
# Example
# all((1, 2, 3, 4, 5), greater_than_9) -> false
# all((1, 2, 3, 4, 5), less_than_9)    -> True

# задача проверит все ли значения в последовательности True
# def _all(seq, fun):
#     return False if False in [fun(i) for i in seq] else True
#
# greater_than_9 = lambda x: x > 9
# less_than_9 = lambda x: x < 9
#
# # 2 очевидно задача на all / any
# def _all(seq, fun):
#     return all(map(fun, seq))
#
# print(_all((1, 2, 3, 4, 5), less_than_9))

# ----------------------------------------------------------------------------------------------------------------------#
# 55  8 kyu / Swap Values

# I would like to be able to pass an array with two elements to my swapValues
# function to swap the values. However it appears that the values aren't changing.
#
# Can you figure out what's wrong here?

# задача поменять местами заначения
# def swap_values(args):
#     args[0], args[1] = args[1], args[0]

# ----------------------------------------------------------------------------------------------------------------------#
# 56  8 kyu / Logical calculator
#
# Your Task
# Given an array of Boolean values and a logical operator, return a
# Boolean result based on sequentially applying the operator to the values in the array.
#
# Examples
# booleans = [True, True, False], operator = "AND"
# True AND True -> True
# True AND False -> False
# return False
# booleans = [True, True, False], operator = "OR"
# True OR True -> True
# True OR False -> True
# return True
# booleans = [True, True, False], operator = "XOR"
# True XOR True -> False
# False XOR False -> False
# return False
# Input
# an array of Boolean values (1 <= array_length <= 50)
# a string specifying a logical operator: "AND", "OR", "XOR"
# Output
# A Boolean value (True or False).

# задача (сложно) вычисляет булево выражение в скобках
# def logical_calc(array, op):
#     if op == 'XOR':
#         op = '^'
#     s = eval(f' {op.lower()} '.join([str(i) for i in array]))
#     return s
#
# print(logical_calc([True, True, False], 'XOR'))

# 2 reduce(func, iter, start=0)
# import operator
# from functools import reduce
#
# def logical_calc(array, op):
#     d = {
#         'AND': operator.and_,
#         'OR': operator.or_,
#         'XOR': operator.xor
#     }
#     return reduce(d[op], array) # берет первые два элемента массива и применяет к ним функцию d[op],
#                                 # потом полученное значение в стаке со следующим и тд
#
# print(logical_calc([True, True, False], 'AND'))

# ----------------------------------------------------------------------------------------------------------------------#
# 57  8 kyu / UEFA EURO 2016

# Finish the uefaEuro2016() function so it return string just like in the examples below:
#
# uefa_euro_2016(['Germany', 'Ukraine'],[2, 0]) # "At match Germany - Ukraine, Germany won!"
# uefa_euro_2016(['Belgium', 'Italy'],[0, 2]) # "At match Belgium - Italy, Italy won!"
# uefa_euro_2016(['Portugal', 'Iceland'],[1, 1]) # "At match Portugal - Iceland, teams played draw."

# задача на сравнение и применение f-строки
# def uefa_euro_2016(teams, scores):
#     if scores[0] == scores[1]:
#         return f'At match {teams[0]} - {teams[1]}, teams played draw.'
#     else:
#         return f'At match {teams[0]} - {teams[1]}, {teams[0] if scores[0] > scores[1] else teams[1]} won!'
#
# print(uefa_euro_2016(['Germany', 'Ukraine'],[2, 2]))

# ----------------------------------------------------------------------------------------------------------------------#
# 58  8 kyu / UEFA EURO 2016

# SpeedCode #2 - Array Madness
# Objective
# Given two integer arrays a, b, both of length >= 1, create a program that returns true if the sum of
# the squares of each element in a is strictly greater than the sum of the cubes of each element in b.
#
# E.g.
#
# array_madness([4, 5, 6], [1, 2, 3]) => True #because 4 ** 2 + 5 ** 2 + 6 ** 2 > 1 ** 3 + 2 ** 3 + 3 ** 3
# Get your timer out. Are you ready? Ready, get set, GO!!!

# def array_madness(a, b):
#     return sum(i ** 2 for i in a) > sum(i ** 3 for i in b)
#
# print(array_madness([4, 5, 6], [1, 2, 3]))

# ----------------------------------------------------------------------------------------------------------------------#
# 59  8 kyu / ???
#
# At the annual family gathering, the family likes to find the oldest living family member’s age and the
# youngest family member’s age and calculate the difference between them.
#
# You will be given an array of all the family members(' ages, in any order. The ages will be given in whole numbers, so a baby '
# 'of 5 months, will have an ascribed ‘age’ of 0. Return a new array (a tuple in Python) with '
#          '[youngest age, oldest age, difference between the youngest and oldest age].)

# def difference_in_ages(ages):
#     return min(ages), max(ages), abs(max(ages) - min(ages))
#
# print(difference_in_ages([16, 22, 31, 44, 3, 38, 27, 41, 88]))

# ----------------------------------------------------------------------------------------------------------------------#
# 60  8 kyu / Merging sorted integer arrays (without duplicates)

# Write a function that merges two sorted arrays into a single one.
# The arrays only contain integers. Also, the final outcome must be sorted and not have any duplicate.

# def merge_arrays(first, second):
#     return sorted(set(first + second))
#
# print(merge_arrays([1, 3, 5], [2, 4, 6]))

# ----------------------------------------------------------------------------------------------------------------------#
# 61  8 kyu / Sort My Textbooks

# HELP! Jason can't find his textbook! It is two days before the test date, and Jason's
# textbooks are all out of order! Help him sort a list (ArrayList in java) full of textbooks by subject,
# so he can study before the test.
#
# The sorting should NOT be case sensitive

# задача отсортировать список без учета регистра. Прикольная
# def sorter(texts):
#     return sorted(texts, key=lambda x: x.lower())
#
# print(sorter(['Algebra', 'history', 'Geometry', 'english']))

# ----------------------------------------------------------------------------------------------------------------------#
# 62  8 kyu / Grasshopper - Array Mean

# Find Mean
# Find the mean (average) of a list of numbers in an array.
#
# Information
# To find the mean (average) of a set of numbers add all of the numbers together and divide by the number of values in the list.
#
# For an example list of 1, 3, 5, 7
#
# 1. Add all of the numbers
#
# 1+3+5+7 = 16
# 2. Divide by the number of values in the list. In this example there are 4 numbers in the list.
#
# 16/4 = 4
# 3. The mean (or average) of this list is 4

# задача найти среднее значение списка
# def find_average(nums):
#     return sum(nums) / len(nums) if nums else 0
#
# print(find_average([1, 3, 5, 7]))

# ----------------------------------------------------------------------------------------------------------------------#
# 63  8 kyu / Short Long Short
#
# Given 2 strings, a and b, return a string of the form short+long+short,
# with the shorter string on the outside and the longer string on the inside.
# The strings will not be the same length, but they may be empty ( zero length ).
#
# Hint for R users:
#
# The length of string is not always the same as the number of characters
# For example: (Input1, Input2) --> output
#
# ("1", "22") --> "1221"
# ("22", "1") --> "1221"

# задача соединить строки как мин + макс + мин
# def solution(a, b):
#     if len(a) > len(b):
#         max_s, min_s = a, b
#     else:
#         max_s, min_s = b, a
#     return f'{min_s}{max_s}{min_s}'

# 2
# def solution(a, b):
#     return a+b+a if len(a) < len(b) else b+a+b
#
# print(solution('U', 'False'))

# ----------------------------------------------------------------------------------------------------------------------#
# 64  8 kyu / Short Long Short (debug)

# Your coworker was supposed to write a simple helper function to capitalize a string
# (that contains a single word) before they went on vacation.
#
# Unfortunately, they have now left and the code they gave you doesn't work.
# Fix the helper function they wrote so that it works as intended (i.e. make the first character in the string "word" upper case).
#
# Don't worry about numbers, special characters, or non-string types being passed to the function.
# The string lengths will be from 1 character up to 10 characters, but will never be empty.

# задача сделать первую букву заглавной
# def capitalize_word(word):
#     return word[0].upper() + word[1:]

# 2 оказывается есть функция для заглавных букв
# def capitalize_word(word):
#     return word.capitalize()
#
# print(capitalize_word('word'))

# ----------------------------------------------------------------------------------------------------------------------#
# 65  8 kyu / Who is going to pay for the wall?

# Don Drumphet lives in a nice neighborhood, but one of his neighbors has started to let his house go. Don Drumphet
# wants to build a wall between his house and his neighbor’s, and is trying to get the neighborhood association to
# pay for it. He begins to solicit his neighbors to petition to get the association to build the wall.
# Unfortunately for Don Drumphet, he cannot read very well, has a very limited attention span, and
# can only remember two letters from each of his neighbors’ names. As he collects signatures,
# he insists that his neighbors keep truncating their names until two letters remain, and he can finally read them.
#
# Your code will show Full name of the neighbor and the truncated version of the name as an array. If the number
# of the characters in name is less than or equal to two, it will return an array containing only the name as is"

# def who_is_paying(name):
#     return [name, name[:2]] if len(name) > 2 else [name]
#
# print(who_is_paying(''))

# ----------------------------------------------------------------------------------------------------------------------#
# 66  8 kyu / Vowel remover

# Create a function called shortcut to remove the lowercase vowels (a, e, i, o, u ) in a given string.
#
# Examples
# "hello"     -->  "hll"
# "codewars"  -->  "cdwrs"
# "goodbye"   -->  "gdby"
# "HELLO"     -->  "HELLO"
# don't worry about uppercase vowels
# y is not considered a vowel for this kata

# задача убрать гласные из слова
# def shortcut(s):
#     return ''.join(i for i in s if i not in {'a', 'e', 'i', 'o', 'u'})
#
# print(shortcut('hello'))

# ----------------------------------------------------------------------------------------------------------------------#
# 67  8 kyu / Contamination #1 -String-

# An AI has infected a text with a character!!
# This text is now fully mutated to this character.
# If the text or the character are empty, return an empty string.
# There will never be a case when both are empty as nothing is going on!!
# Note: The character is a string of length 1 or an empty string.
#
# Example
# text before = "abc"
# character   = "z"
# text after  = "zzz"

# def contamination(text, char):
#     return len(text) * char
#
# print(contamination('abc', 'z'))

# ----------------------------------------------------------------------------------------------------------------------#
# 67  8 kyu / Up and down, the string grows

# Write a function that returns a string in which firstname is swapped with last name.
#
# Example(Input --> Output)
#
# "john McClane" --> "McClane john"

# задача поменять местами слова в строке
# def name_shuffler(str_):
#     return ' '.join(str_.split()[::-1])
#
# print(name_shuffler('john McClane'))

# ----------------------------------------------------------------------------------------------------------------------#
# 68  8 kyu / DNA to RNA Conversion

# задача земенить букву
# def dna_to_rna(dna):
#     return dna.replace('T', 'U')
#
# print(dna_to_rna('TTT'))

# ----------------------------------------------------------------------------------------------------------------------#
# 69  8 kyu / DNA to RNA Conversion
#
# Make a function that will return a greeting statement that uses an input;
# your program should return, "Hello, <name> how are you doing today?".
#
# [Make sure you type the exact thing I wrote or the program may not execute properly]

# def greet(name):
#     return f"Hello, {name} how are you doing today?"
#
# print(greet('b'))

# ----------------------------------------------------------------------------------------------------------------------#
# 70  8 kyu / Abbreviate a Two Word Name

# Write a function to convert a name into initials. This kata strictly takes two words with one space in between them.
# The output should be two capital letters with a dot separating them.
# It should look like this:
# Sam Harris => S.H
# patrick feeney => P.F

# задача вернуть инициалы имени и фамилии. Этот вариант подойдет только если был ввод с заглавной буквы
# def abbrev_name(name):
#     return '.'.join(i for i in name if i.isupper())

# 2
# def abbrev_name(name):
#     lst = name.split()
#     return f'{lst[0][0].upper()}.{lst[1][0].upper()}'
#
#
# print(abbrev_name('Sam Harris'))

# ----------------------------------------------------------------------------------------------------------------------#
# 71  8 kyu / Is the string uppercase?

# задача проверить написаны ли все слова капсом в строке
# def is_uppercase(inp):
#     return not bool(''.join(i for i in inp if i.islower()))

# 2 есть попроще варик
# def is_uppercase(inp):
#     return inp.upper() == inp
#
# print(is_uppercase('HELLO'))

# ----------------------------------------------------------------------------------------------------------------------#
# 72  8 kyu /
