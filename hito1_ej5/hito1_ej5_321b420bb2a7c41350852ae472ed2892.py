#calculo del digito verificador del rut

rut = int(input("ingrese el rut:"))
print("descomposicion del rut:", rut//10000000)
print("descomposicion del rut:", rut//1000000)
print("descomposicion del rut:", rut//100000)
print("descomposicion del rut:", rut//10000)
print("descomposicion del rut:", rut//1000)
print("descomposicion del rut:", rut//100)
print("descomposicion del rut:", rut//10)
print("descomposicion del rut:", rut//1)
a= (rut//10000000) * 3
print("resultado de a:",a)
b= ((rut//1000000)%10) * 2
print("resultado de b:",b)
c= ((rut//100000)%10) * 7
print("resultado de c:",c)
d= ((rut//10000)%10) * 6
print("resultado de d:",d)
e= ((rut//1000)%10) * 5
print("resultado de e:",e)
f= ((rut//100)%10) * 4
print("resultado de f;",f)
g= ((rut//10)%10) * 3
print("resultado de g:",g)
h= ((rut//1)%10) * 2
print("resultado de h:",h)
suma = (a+b+c+d+e+f+g+h)
print("la resultado de la suma: ",suma)
resto1= suma//11
print("resuktado de la resto1=suma//11:",resto1)
resto2=suma-(11*resto1)
print("resultado de la resto2=suma-(11*resto1):",resto2)
resta=11-resto2
print("resultado de la resta =11-resto2:",resta)
if resta==11:
    print("dv=", end="")
    print(0)
elif resta==10:
    print("dv=",end="")
    print("k")
else:
     print("dv=",end="")
     print(resta)

