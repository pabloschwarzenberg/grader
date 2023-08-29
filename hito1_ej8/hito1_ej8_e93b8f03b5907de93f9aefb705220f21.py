#Descomponer un número
numero = int(input("ingrese un numero de hasta 4 cifras: "))
if numero < 10:
    print(numero,"U", sep="")
    
if 100 > numero > 9:
    i = numero%10
    j=numero/10
    n= int(j)
    print(n,"D"," ","+"," ",i,"U",sep="")
    
if 99 < numero < 1000:
    r= numero%10
    s= numero%100
    t= int(s)
    u= t/10
    v= int(u)
    p=numero/100
    q= int(p)
    print(q,"C"," ","+"," ",v,"D"," ","+"," ",r,"U",sep="")
    
if 1000<= numero < 10000:
    a= numero%10
    b= numero%100
    c= int(b)
    d= c/10
    e= int(d)
    f=numero/100
    g= int(f)
    h= g%10
    x= g/10
    y= int(x)
    print(y,"M"," ","+"," ",h,"C"," ","+"," ",e,"D"," ","+"," ",a,"U",sep="")