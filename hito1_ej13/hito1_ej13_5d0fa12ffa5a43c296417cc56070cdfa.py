numero = int(input('ingrese un numero: '))

for i in [2,3,5,7,9,11,13]:
    a = numero%i

    if(a == 0):
        print(i)