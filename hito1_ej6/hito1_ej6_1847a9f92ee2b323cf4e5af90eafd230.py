a=int(input("Ingrese su primer numero :"))
b=int(input("Ingrese su segundo numero :"))
c=int(input("Ingrese su tercer numero :"))

if a<b :
    if b<c :
        print(a,",",b,",",c)
        
    elif c<a :
        print(c,",",a,",",b)
    else :
        print(a,",",c,",",b)
elif b<a :
    if a<c :
        print(b,",",a,",",c)
    elif c<b :
        print(c,",",b,",",a)
    else :
        print(b,",",c,",",a)
