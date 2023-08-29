#Aprobación de créditos
IN=int(input("ingresos :"))
ano=int(input("Año de nacimiento :"))
hijos=int(input("Número de hijos :"))
ban=int(input("Años de pertenencia al banco :"))

sol=str(input("S: soltero, C: casado  :"))
zona=str(input("U: urbano, R: rural  :"))
edad=2021-ano

if ban >10 and hijos >=2:
    resultado="APROBADO"
elif(sol=="C" and hijos>3 and (edad>=45 and edad<=55)) :   
    resultado="APROBADO"
elif(IN >=2500000 and sol=="S" and zona =="U"):   
    resultado="APROBADO"
elif(IN>350000 and ban>=5):
     resultado="APROBADO"
elif(sol=="S" and zona =="R" and hijos <2):
     resultado="APROBADO"
else:
     resultado ="RECHAZADO"     
        
print(resultado)    