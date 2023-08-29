#Aprobación de créditos
ing=int(input())
ano=int(input())
hijos=int(input())
banco=int(input())
estado=str(input())
vive=str(input())

if(((banco>10)and(hijos>=2))
or((estado=="C")and(hijos>=3)and(1962<=ano<=1972)
or((ing>=2500000)and(estado=="S")and(vive=="U"))
or((ing>=3500000)and(banco>5))
or((vive=="R")and(estado=="C")and(hijos<2)))):
     print("APROBADO")
else:
     print("RECHAZADO")     