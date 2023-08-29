#Descomponer un número
n=str(input("ingrese un num max de 4 digitos: "))
if len(n)==4:
    m=n[0]
    m+="M"
    c=n[1]
    c+="C"
    d=n[2]
    d+="D"
    u=n[3]
    u+="U"
    print(m,"+",c,"+",d,"+",u)
elif len(n)==3:
    c=n[0]
    c+="C"
    d=n[1]
    d+="D"
    u=n[2]
    u+="U"
    print(c,"+",d,"+",u)
elif len(n)==2:
    d=n[0]
    d+="D"
    u=n[1]
    u+="U"
    print(d,"+",u)
elif len(n)==1:
    u=n[0]
    u+="U"
    print(u)


      