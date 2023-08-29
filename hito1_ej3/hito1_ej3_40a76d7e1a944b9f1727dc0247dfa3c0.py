ingreso=int(input("ingreso en pesos: "))
nacimiento=int(input("año de nacimiento: "))
hijos=int(input("cantidad de hijos: "))
antiguedad=int(input("años de pertenencia al banco: "))
edad=nacimiento-2022

print(" escriba S si es soltero y C si es casado ")
estado=str(input("estado civil: "))

print(" escriba U si es urbano y R si es rural ")
vivienda=str(input("vive en campo o cuidad: "))

if( antiguedad>10 and hijos>=2 ):
    print("APROBADO")
elif( estado=="C" and hijos>3 and edad>=45 and edad<=55 ):
    print("APROBADO")
elif( ingreso>=2500000 and estado=="S" and vivienda=="U" ):
    print("APROBADO")
elif( ingreso>3500000 and antiguedad>5 ):
    print("APROBADO")
elif( vivienda=="R" and estado=="C" and hijos<2 and hijos>0):
    print("APROBADO")
else:
    print("RECHAZADO")