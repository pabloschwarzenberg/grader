#Aprobación de créditos
print("Requisitos para aprobación de créditos")
ingreso=float(input("Ingresos: "))
ano=int(input("Año de nacimiento: "))
hijo=int(input("Cantidad de hijos: "))
pert=int(input("Años de pertenencia al banco: "))
ec=input("Estado civil: ")
vive=input("Donde vive: ")
edad=(2016-ano)
if(pert>=10)and(hijo>=2):
    print("APROBADO")
elif(ec=="C")and(hijo>3)and(45<=edad<=55):
    print("APROBADO")
elif(ingreso>=2500000)and(ec=="S")and(vive=="U"):
    print("APROBADO")
elif(ingreso>=3500000)and(pert>5):
    print("APROBADO")
elif(vive=="R")and(ec=="C")and(hijo<=2):
    print("APROBADO")
else:
    print("RECHAZADO")
