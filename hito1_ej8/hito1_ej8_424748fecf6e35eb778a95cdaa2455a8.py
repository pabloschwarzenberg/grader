#Descomponer un número
n=input('ingresa un numero de hasta 4 digitos:')
n=int(n)
if n>=1000 :
    n=str(n)
    a=n[0]
    b=n[1]
    c=n[2]
    d=n[3]
    print(a,'M' '+ ',b,'C' '+' ,c,'D' '+' ,d,'U' )
elif n<1000 and n>=100:
    n=str(n)
    b=n[0]
    c=n[1]
    d=n[2]
    print(b,'C' '+' ,c,'D' '+' ,d,'U' )
elif n<100 and n>=10:
    n=str(n)
    c=n[0]
    d=n[1]
    print(c,'D' '+' ,d,'U' )
elif n<10 and n>=0:
    d=n[0]
    print(d,'U' )