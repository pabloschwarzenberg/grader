#Descomponer un número
num = input('Ingrese un número de hasta 4 dígitos: ')

while not len(str(num)) <= 4 and len(str(num)) >= 1 :
    n = int(input('Ingrese un número de hasta 4 dígitos: '))

if len(str(num)) == 4:
    a = int(num[0])
    b = int(num[1])
    c = int(num[2])
    d = int(num[3])
    print(a,'M +',b,'C +',c,'D +',d,'U')
elif len(str(num)) == 3:
    a = int(num[0])
    b = int(num[1])
    c = int(num[2])
    print(a,'C +',b,'D +',c,'U')
elif len(str(num)) == 2:
    a = int(num[0])
    b = int(num[1])
    print(a,'D +',b,'U')
else:
    a = int(num[0])
    print(a,'U')