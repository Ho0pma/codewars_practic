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

def multiple_of_index(arr):
    pass











