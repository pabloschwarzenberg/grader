#Descomponer un número
num = input('Numero: ')
largo = len(num)
num = list(num)

l = ['M+','C+','D+','U']

descomp = []

i = 0
while i<largo:
    descomp.extend(num[i]+l[i+4-largo])
    i=i+1

print(descomp)

n = ''.join(descomp)

print(n)
