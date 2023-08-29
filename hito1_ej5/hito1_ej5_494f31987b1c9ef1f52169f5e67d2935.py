#Cálculo del dígito verificador de un rut
rut=int(input("Ingrese su RUN:"))
print("Descomposicion del rut", rut//10000000)
print("Descomposicion del rut", rut//1000000)
print("Descomposicion del rut", rut//100000)
print("Descomposicion del rut", rut//10000)
print("Descomposicion del rut", rut//1000)
print("Descomposicion del rut", rut//100)
print("Descomposicion del rut", rut//10)
print("Descomposicion del rut", rut//1)
a=(rut//10000000)*3
print("Resultado de a:", a)
b=((rut//1000000)%10)*2
print("Reseultado de b:", b)
c=((rut//100000)%10)*7
print("Reseultado de b:", c)
d=((rut//10000)%10)*6
print("Reseultado de b:", d)
e=((rut//1000)%10)*5
print("Reseultado de b:", e)
f=((rut//100)%10)*4
print("Reseultado de b:", f)
g=((rut//10)%10)*3
print("Reseultado de b:", g)
h=((rut//1)%10)*2
print("Reseultado de b:", h)
suma=(a+b+c+d+e+f+g+h)
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




   