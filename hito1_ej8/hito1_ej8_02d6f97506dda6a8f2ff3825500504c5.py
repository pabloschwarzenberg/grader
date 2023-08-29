#Descomponer un número
n= input("Ingrese un numero de hasta 4 digitos: ")
i= len(n)

if i == 4:
    m=n[0]+"m"
    c=n[1]+"C"
    d=n[2]+"D"
    u=n[3]+"U"
    print (m,"+",c,"+",d,"+",u)
elif  i == 3:
    c=n[0]+"C"
    d=n[1]+"D"
    u=n[2]+"U"
    print  (c,"+",d,"+",u)
elif  i == 2:
    d=n[0]+"D"
    u=n[1]+"U"
    print   (d,"+",u)
elif  i == 1:
    u=n[0]+"U"
    print (u)

