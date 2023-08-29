#Aprobación de créditos
sueldo=int(input("Ingrese su sueldo(en pesos):"))
cumple=int(input("Ingrese su año de nacimiento:"))
hijos=int(input("Cuantos hijos tienes:"))
anosp=int(input("Cuantos años lleva en el banco?:"))
estado=input("Ingrese si es casado con la letra C o soltero con la letra S:")
vive=input("Si donde vive es rural ingrese una R y si es urbano ingrese una U:")
edad=cumple-2022

if anosp > 10 and hijos >= 2:
    print("APROBADO")
elif estado=="C" and hijos > 3 and 45 < edad > 55:
    print("APROBADO")
elif sueldo > 2500000 and estado=="S" and vive=="U":
    print("APROBADO")
elif sueldo > 3500000 and anosp > 5:
    print("APROBADO")
elif vive=="R" and estado=="C" and hijos < 2:
    print("APROBADO")
else: 
    print("RECHAZADO") 