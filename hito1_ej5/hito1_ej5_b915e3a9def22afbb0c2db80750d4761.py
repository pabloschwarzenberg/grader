#Cálculo del dígito verificador de un rut
rut=int(input("Ingrese su rut: "))

uno=(rut//10000000) * 3
dos=((rut//1000000)%10) * 2
tres=((rut//100000)%10) * 7
cuatro=((rut//10000)%10) * 6
cinco=((rut//1000)%10) * 5
seis=((rut//100)%10) * 4
siete=((rut//10)%10) * 3
ocho=((rut//1)%10) * 2
mas=(uno+dos+tres+cuatro+cinco+seis+siete+ocho)
menos1= mas // 11
menos2=mas-(11*menos1)
menos=11-menos2
if menos == 11:
    print("dv=",end="")
    print(0)
elif menos == 10:
    print("dv=",end="")
    print("k")
else:
    print("dv=",end="")
print(menos)