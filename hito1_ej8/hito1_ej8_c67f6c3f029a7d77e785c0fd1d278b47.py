n=int(input())
p=str(n)
unidades=str((n%10)//1)
decenas=str((n%100)//10)
centenas=str((n%1000)//100)
miles=str((n%10000)//1000)

u=unidades + "U"
d=decenas + "D"
c=centenas + "C"
m=miles + "M"

if len(p)<=4:
    if int(decenas)==0:
        print(u)
    elif int(centenas)==0:
        print(d,"+",u)
    elif int(miles)==0:
        print(c,"+",d,"+",u)
    else:
        print(m,"+",c,"+",d,"+",u)
else:
    print("el numero no puede tener mas de 4 digitos") 