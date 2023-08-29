#Cálculo del dígito verificador de un rut
rut=str(input("ingrese su rut sin el digito verificador"))
largo=len(rut)
digito=largo-1
a=range(largo)
dig=0
for n in a:
    if (n==6):
        dig=dig+(int(rut[digito])*2)
        digito=digito-1
    elif (n==7):
        dig=dig+(int(rut[digito])*3)
        digito=digito-1
    else:
        dig=dig+(int(rut[digito])*(n+2))
        digito=digito-1
dig=dig%11
dig=11-dig
if(dig>=11):
    print("dv=0")
elif(dig==10):
    print("dv=K")
else:
    print("dv=",dig)    