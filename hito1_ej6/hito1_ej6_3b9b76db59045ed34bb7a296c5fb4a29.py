#Ordenar tres números
print('Ingrese 3 numeros enteros: ')

x1=int(input('Ingrese el primer numero: '))
x2=int(input('Ingrese el segundo numero: '))
x3=int(input('Ingrese el tercer numero: '))

if x1==x2==x3:
    print(x3,', ',x2,', ',x1)
if x1!=x2!=x3:
    if x1>x2 and x1>x3:
        if x2>x3:
            print(x3,', ',x2,', ',x1)
        elif x2<x3:
            print(x2,', ',x3,', ',x1)
    if x2>x1 and x2>x3:
        if x1>x3:
            print(x3,', ',x1,', ',x2)
        elif x1<x3:
            print(x1,', ',x3,', ',x2)
    if x3>x1 and x3>x2:
        if x2>x1:
            print(x1,', ',x2,', ',x3)
        elif x2<x1:
            print(x2,', ',x1,', ',x3)
if x1==x2:
    if x1>x3:
        print(x3,', ',x1,', ',x2)
    elif x3>x1:
        print(x1,', ',x2,', ',x3)
if x1==x3:
    if x1>x2:
        print(x2,', ',x1,', ',x3)
    elif x2>x1:
        print(x1,', ',x3,', ',x2)
if x3==x2:
    if x1>x3:
        print(x3,', ',x2,', ',x1)
    elif x3>x1:
        print(x1,', ',x2,', ',x3)