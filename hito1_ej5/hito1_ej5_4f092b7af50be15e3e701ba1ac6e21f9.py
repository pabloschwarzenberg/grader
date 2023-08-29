#Cálculo del dígito verificador de un rut
import operator
import math

rut=input("Ingrese su rut sin dv: ")
rutlist=[]
numcal=[3,2,7,6,5,4,3,2]

for i in rut:
  rutlist.append(i)

rutlistint=[int(x) for x in rutlist]
calculo=list(map(operator.mul, rutlistint, numcal))

calculo1=sum(list(calculo))
calculo2=math.floor(calculo1/11)
calculo3=calculo1-(11*calculo2)
calculo4=11-calculo3
digitorverificador=calculo4

if(calculo4==1):
  digitorverificador="0"
  
if(calculo4==10):
  digitorverificador="k"

print("El digito verificador es: ",digitorverificador)