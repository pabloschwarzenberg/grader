#Cálculo del dígito verificador de un rut
rut=int(input("Ingrese el rut: "))
print("descomponer rut")
print("descomposición del rut ", rut//10000000)
print("descomposición del rut ", rut//1000000)
print("descomposición del rut ", rut//100000)
print("descomposición del rut ", rut//10000)
print("descomposición del rut ", rut//1000)
print("descomposición del rut ", rut//100)
print("descomposición del rut ", rut//10)
print("descomposición del rut ", rut//1)
m1=(rut//10000000) * 3
m2=((rut//1000000)%10) * 2
m3=((rut//100000)%10) * 7
m4=((rut//10000)%10) * 6
m5=((rut//1000)%10) * 5
m6=((rut//100)%10) * 4
m7=((rut//10)%10) * 3
m8=((rut//1)%10) * 2
suma=(m1+m2+m3+m4+m5+m6+m7+m8)
print("resultado de la suma: ",suma)
resto1= suma // 11
print("resultado de la resto1=suma // 11: ",resto1)
resto2=suma-(11*resto1)
print("resultado de la resto2=suma-(11*resto1): ",resto2)
resta=11-resto2
print("resultado de la resta=11-resto2: ",resta)
if resta == 11:
    print("dv=",end="")
    print(0)
elif resta == 10:
    print("dv=",end="")
    print("k")
else:
    print("dv=",end="")
    print(resta)