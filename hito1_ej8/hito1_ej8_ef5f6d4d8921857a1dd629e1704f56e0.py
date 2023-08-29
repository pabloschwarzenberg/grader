#Descomponer un número
num = input('Ingrese un número: ')
units = ['M', 'C', 'D', 'U']
i = len(num) - 1
j = 3
answer = ''
while i >= 0:
  if i != len(num) - 1:
    suffix = '+' + answer
  else:
    suffix = answer
  answer = num[i] + units[j] + suffix
  i -= 1
  j -= 1
  
print(answer)