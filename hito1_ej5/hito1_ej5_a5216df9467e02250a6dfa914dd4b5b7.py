#Cálculo del dígito verificador de un rut
rut_usuario=int(input("Ingrese el rut: "))
a=(rut_usuario//10000000) * 3
b=((rut_usuario//1000000)%10) * 2
c=((rut_usuario//100000)%10) * 7
d=((rut_usuario//10000)%10) * 6
e=((rut_usuario//1000)%10) * 5
f=((rut_usuario//100)%10) * 4
g=((rut_usuario//10)%10) * 3
h=((rut_usuario//1)%10) * 2
suma=(a+b+c+d+e+f+g+h)
resto_1= suma // 11
resto_2=suma-(11*resto_1)
resta=11-resto_2
if resta == 11:
    print("dv=",end="")
    print(0)
elif resta == 10:
    print("dv=",end="")
    print("k")
else:
    print("dv=",end="")
    print(resta)