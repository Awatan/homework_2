#1
first = int(input('First one: '))
second = int(input('Second: '))
if first > second:
   print('The first is bigger')
elif first < second:
   print('The second is bigger')
else:
   print('They are the same')

#2
a = int(input('First: '))
b = int(input('Second: '))
c = int(input('Third: '))
if a == b or a == c or b == c:
   print(a + 5, b + 5, c + 5)
else:
   print('Not the same')

#3
for i in range(9):
   for j in range(9):
       print(i + 1, '*', j + 1, '=', (i + 1) * (j + 1))

#4
print('triangle')
for i in range(6):
   print('*' * i)

print('kvadrat')
m = 4
for i in range(m):
   i ='&' * 2 * m
   print(i)

print('romb')
n = 6
for x in range(n):
    print(' ' * (n - x), '*' * (x + 1), '*' * x, sep='')
for x in reversed(range(n)):
    print(' ' * (n - x), '*' * (x + 1), '*' * x, sep='')

print('5-kytnuk')
o = 6
for x in range(o):
    print(' ' * (o - x), '*' * x, '*' * x, sep='')
for x in reversed(range(o)):
    print(' ' * (o - x), '*' * x, '*' * x, sep='')

print('elka')
n = 6
for x in range(n):
    print(' ' * (n - x), '*' * (x + 1), '*' * x, sep='')

print('stypenka')
n = 22
for x in range(2, n, 3):
    print('*' * x)
    print('*' * x)

#5
student = input('Who are you: ')
group = input('Yours group:')
line_2 = '*Лабораторная работа н1'
line_3 = '*Выполнил(а): ст. гр.' + group
line_4 = '*' + student
longest = [line_2, line_3, line_4]
longest_line = (max(longest, key=len))
size_longest = int(len(longest_line))
size_2 = size_longest - int(len(line_2))
size_3 = size_longest - int(len(line_3))
size_4 = size_longest - int(len(line_4))
print('*' * size_longest + '**')
print(line_2, ' ' * size_2 + '*')
print(line_3, ' ' * size_3 + '*')
print(line_4, ' ' * size_4 + '*')
print('*' * size_longest + '**')

#5 with for
student = input('Who are you: ')
group = input('Yours group:')
line_2 = '*Лабораторная работа н1'
line_3 = '*Выполнил(а): ст. гр.' + group
line_4 = '*' + student
longest = [line_2, line_3, line_4]
longest_line = (max(longest, key=len))
size_longest = int(len(longest_line))
print('*' * size_longest + '*')
for i in range(len(longest)):
    print(longest[i], ' ' * (size_longest - int(len(longest[i]))), '*', sep='')
print('*' * size_longest + '*')