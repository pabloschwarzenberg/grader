#Aprobación de créditos
ingreso= int(input("Indique su ingreso neto en pesos"))
ano= int(input("año de nacimiento:"))
N= int(input("numero de hijos:"))
pert= int(input("años de pertenencia al banco:"))
est=input("estado civil:")
sec= input("campo o ciudad")
B= "APROBADO"
X= "RECHAZADO"
if 10<pert and 2<=N:
  a=B
elif est=="C" and 3<N and 45<ano<55:
  a=B
elif 2500000<ingreso and est== "S" and sec=="U":
  a=B
elif 3500000<ingreso and 5<pert:
  a=B
elif sec=="R" and est=="C" and N<2:
   a=B
else:
  a=X
print(a)