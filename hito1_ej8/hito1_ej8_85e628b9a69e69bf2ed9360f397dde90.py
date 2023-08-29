#Descomponer un número
s=input("Ingrese número de 4 digitos: ")
if int(s)>=1000:
    b1=s[0]+"M"
    b2=s[1]+"C"
    b3=s[2]+"D"
    b4=s[3]+"U"
    print(b1,"+",b2,"+",b3,"+",b4)
elif int(s)<=999 and int(s)>=100:
    b1=s[0]+"C"
    b2=s[1]+"D"
    b3=s[2]+"U"
    print(b1,"+",b2,"+",b3)
elif int(s)<=99 and int(s)>=10:
    b1=s[0]+"D"
    b2=s[1]+"U"
    print(b1,"+",b2)
else:
     b1=s[0]+"U"
     print(b1)