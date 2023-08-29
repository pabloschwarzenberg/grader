numero = int(input('ingrese un numero de 4 digitos: '))

cantidad = len(str(numero))

if(cantidad==4):
    a = numero//1000
    restoa = numero%1000
    b = restoa//100
    restob = restoa%100
    c = restob//10
    d = restob%10

    print(str(a)+'M +', str(b)+'C +', str(c)+'D +', str(d)+'U')

if(cantidad==3):
    a = numero//100
    restoa = numero%100
    b = restoa//10
    c = restoa%10

    print(str(a)+'C +', str(b)+'D +', str(c)+'U')

if(cantidad==2):
    a = numero//10
    b = numero%10

    print(str(a)+'D +', str(b)+'U')
    
if(cantidad==1):

    print(str(numero)+'U')