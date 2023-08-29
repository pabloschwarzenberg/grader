#Cálculo del dígito verificador de un rut
rut=int(input("ingrese el rut:"))
print("descomponer rut")
print("descomposicion de rut",rut//10000000)
print("descomposicion de rut",rut//1000000)
print("descomposicion de rut",rut//100000)
print("descomposicion de rut",rut//10000)
print("descomposicion de rut",rut//1000)
print("descomposicion de rut",rut//100)
print("descomposicion de rut",rut//10)
print("descomposicion de rut",rut//1)
a=(rut//10000000) * 3
print("el resultado de a:",a)
b=(rut//1000000)%10*2
print("el resultado de b:",b)
c=(rut//100000)%10*7
print("el resultado de c es:",c)
d=(rut//10000)%10*6
print("el resultado de d es:",d)
e=(rut//1000)%10*5
print("el resultado de e es:",e)
f=(rut//100)%10*4
print("el resultado de f es:",f)
g=(rut//10)%10*3
print("el resultado de g es:",g)
h=(rut//1)%10*2
print("el resultado de h es:",h)
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