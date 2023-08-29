#Descomponer un número
num=int(input("ingrese un numero de hasta 4 digitos"))
lar=len(str(num))
if lar==1:
    num=int(num)
    a=str(num%10)
    a=a+"U"
    print(a)
elif lar==2:
    num=int(num)
    a=str(num%10)
    a1=a+"U"
    a=int(a)
    num=int(num)
    num=num-a
    num=int(num//10)
    b=str(num%10)
    b2=b+"D"
    print(b2 ,"+",a1 )
elif lar==3:
    num=int(num)
    a=str(num%10)
    a1=a+"U"
    a=int(a)
    num=int(num)
    num=num-a
    num=int(num//10)
    b=str(num%10)
    b2=b+"D"
    b=int(b)
    num=int(num)
    num=num-b
    num=int(num//10)
    c=str(num%10)
    c3=c+"C"
    print(c3 ,"+", b2 ,"+", a1)
elif lar==4:
    num=int(num)
    a=str(num%10)
    a1=a+"U"
    a=int(a)
    num=int(num)
    num=num-a
    num=int(num//10)
    b=str(num%10)
    b2=b+"D"
    b=int(b)
    num=int(num)
    num=num-b
    num=int(num//10)
    c=str(num%10)
    c3=c+"C"
    c=int(c)
    num=int(num)
    num=num-c
    num=int(num//10)
    d=str(num%10)
    d4=d+"M"
    print(d4 ,"+", c3 ,"+", b2 ,"+", a1)
 
 