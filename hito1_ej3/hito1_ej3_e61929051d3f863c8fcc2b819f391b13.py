#Aprobación de créditos
Soltero="S"
Casado="C"
Rural="R"
Urbana="U"
Gana=float(input("Cuato gana?:"))
Nacio=int(input("En que año nacio?:"))
N_hijos=int(input("Cuantos hijos tiene?:"))
Anos_banco=int(input("Cuantos años lleva en el banco?:"))
Estado_civil=(input("Es soltero[S] o casado[C]:"))
Donde_vive=input("Vive en sona Urbana[U] o Rural[R]:")

Edad=2020-Nacio

if (Anos_banco>10 and N_hijos>2):
   print("APROBADO")
elif (Estado_civil==Casado and N_hijos>3 and Edad<=55 and Edad>=45):
    print("APROBADO")
elif (Gana>2500000 and Estado_civil==Soltero and Donde_vive==Urbana):
    print("APROBADO")
elif (Gana>35000000 and Anos_banco>5):
    print("APROBADO")
elif (Donde_vive==Rural and N_hijos<2 and Estado_civil==Casado):
    print("APROBADO")
else:
    print("RECHAZADO")  