import math
rut=int(input("RUT: "))
a=0
d=int(math.log10(rut))+1

for n in range(1,d+1,6):              #Módulo (6) de coeficientes del rut
    for i in range(2,8):            #Considera intervalos de 2 a 7
        a=(rut%10**(i+n-2)-rut%10**(i+n-3))*i/10**(i+n-3)+a     #Considera cada dígito, multiplica por i y suma con anteriores

d=11-a%11
if d==10:
    print("dv=k")
elif d==11:
    print("dv=0")
else:
    print("dv=",d)