#Descomponer un número
number = int(input())
n = len(str(number))
a = 10**n
b = (10**n) / 10
lst = ['M', 'C', 'D', 'U']
result = ''
count = len(lst) - n
for i in range(n):
    digit = number % a // b
    result += str(int(digit)) + lst[count]
    count += 1
    a /= 10
    b /= 10
    if i == n-1:
        break
    result += '+'
print(result)