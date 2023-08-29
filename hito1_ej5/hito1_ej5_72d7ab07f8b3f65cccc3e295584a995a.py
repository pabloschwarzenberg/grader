#Cálculo del dígito verificador de un rut
rut=int(input("ingrese un numero: "))

rut1= rut % 10*2
rut2= rut //10 % 10*3
rut3= rut //100 % 10*4
rut4= rut //1000 % 10*5
rut5= rut //10000 % 10*6
rut6= rut //100000 % 10*7
rut7= rut //1000000 % 10*2
rut8= rut //10000000 % 10*3
rut9= rut //100000000 % 10*4
rut0= rut //1000000000 % 10*5

suma= rut1+rut2+rut3+rut4+rut5+rut6+rut7+rut8+rut9+rut0

modulo= suma//11
resto= suma-(11*modulo)
rfinal = 11-resto
if rfinal== 11:
    print("dv=0")
elif rfinal== 10:
    print("dv=K")
else:
    print("dv=",rfinal)