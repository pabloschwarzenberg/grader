#Descomponer un número
x=int(input('ingrese un numero de hasta 4 digitos:'))
if 0<x<10:
    print(str(x)+'U')
elif 10<=x<100:
    m=x%10
    n=x//10
    print(str(n)+'D','+',str(m)+'U')
elif 100<=x<1000:
    a=x%10
    b=(x//10)%10
    c=x//100
    print(str(c)+'C','+',str(b)+'D','+',str(a)+'U')
elif 1000<=x<10000:
    s=x%10
    p=(x//10)%10
    d=(x//100)%10
    f=x//1000
    print(str(f)+'M','+',str(d)+'C','+',str(p)+'D','+',str(s)+'U')
else:
    print('ERROR')      