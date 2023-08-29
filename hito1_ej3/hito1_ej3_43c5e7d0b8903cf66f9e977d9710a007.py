#Aprobación de créditos
print("Ingrese su ingreso en pesos: ")
Ingreso=int(input())
print("Ingrese su año de nacimiento: ")
Edad=int(input())
print("Ingrese numero de hijos: ")
Hijos=int(input())
print("ingresar cuantos años lleva en el banco: ")
Cliente=int(input())
print("Ingrese estado civil")
print("S=Soltero, C=Casado")
EstadoCivil=str(input())
print("Indique su direccion U=Urbano, R=Rural")
print("Indicar su direccion: ")
Direccion=str(input())



if (Cliente>10 and Hijos >=2):
 print("Su credito es APROBADO")
else:
    if (EstadoCivil== "C" and Hijos>3 and 45<=Edad<=55):
     print("Su credito es APROBADO")
    else:
        if (Ingreso>2500000 and EstadoCivil== "S" and Direccion== "U"):
         print("Su credito es APROBADO")
        else:
            if (Ingreso>3500000 and Cliente>5):
             print("Su credito es APROBADO")
            else:
                if (Direccion== "R" and EstadoCivil== "C" and Hijos<2):
                 print("Su credito es APROBADO")
                else:
                 print("Su credito es RECHAZADO")
     
     

    