rut = str(input("ingrese su rut sin digito verificador: "))
m=2
i=len(rut)-1
paso1=0
while i>=0:
    paso1+=int(rut[i])* m
    i-=1
    m+=1
    if m>7:
        m=2
paso2 = paso1//11
paso3=paso1-11*paso2
paso4 = 11 - paso3
if paso4==11:
    print("dv=0")
elif paso4==10:
    print("dv=k")
else:
    print("dv=", paso4)
