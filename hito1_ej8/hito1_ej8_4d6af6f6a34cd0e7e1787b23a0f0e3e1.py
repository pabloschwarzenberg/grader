#Descomponer un número
n=input("Ingrese número de hasta 4 dígitos:")
n=str(n)

if int(n)>999:
    u=n[3]+"U"
    d=n[2]+"D"
    c=n[1]+"C"
    m=n[0]+"M"

    print(m,"+",c,"+",d,"+",u)

elif int(n)>99:
    u=n[2]+"U"
    d=n[1]+"D"
    c=n[0]+"C"

    print(c,"+",d,"+",u)

elif int(n)>9:
    u=n[1]+"U"
    d=n[0]+"D"

    print(d,"+",u)

elif int(n)<9:
    u=n[0]+"U"


    print(u)