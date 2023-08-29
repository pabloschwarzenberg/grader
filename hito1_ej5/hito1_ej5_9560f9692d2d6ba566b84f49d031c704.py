rut=int(input("ingrese rut sin digito verificador: "))


digitos=((rut%10)*2)
digitos1 = (rut%100)
digitos11=(digitos1//10)*3
digitos2 = (rut%1000)
digitos22= (digitos2//100)*4
digitos3=(rut%10000)
digitos33=(digitos3//1000)*5
digitos4=(rut%100000)
digitos44=(digitos4//10000)*6
digitos5=(rut%1000000)
digitos55=(digitos5//100000)*7
digitos6=(rut%10000000)
digitos66=(digitos6//1000000)*2
digitos7=(rut%100000000)
digitos77=(digitos7//10000000)*3

s=(digitos+digitos11+digitos22+digitos33+digitos44++digitos55+digitos66+digitos77)

division1=(s//11)
division2=(s-(11*division1))

dv=(11-division2)

if dv==11:
    print("dv=0")
elif dv==10:
    print("dv="+str("k"))
else:
    print("dv="+str(dv))
