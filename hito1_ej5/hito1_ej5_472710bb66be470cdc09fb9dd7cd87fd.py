verificador = int(input("Ingrese el rut: "))
Z=(verificador//10000000) * 3
Y=((verificador//1000000)%10) * 2
X=((verificador//100000)%10) * 7
V=((verificador//10000)%10) * 6
R=((verificador//1000)%10) * 5
L=((verificador//100)%10) * 4
H=((verificador//10)%10) * 3
F=((verificador//1)%10) * 2
operacion=(Z+Y+X+V+R+L+H+F)
operacion_2= operacion // 11
operacion_23=operacion-(11*operacion_2)
Resta=11-operacion_23
if Resta == 11:
    print("dv=",end="")
    print(0)
elif Resta == 10:
    print("dv=",end="")
    print("k")
else:
    print("dv=",end="")
    print(Resta)
      