
import math
Ingreso= int(input("Ingreso en pesos:"))
Año= int(input("Año de nacimiento:"))
Hijos= int(input("Numero de hijos:"))
Pertenencia= int(input("Años de pertenencia al banco:"))
Estado= input("Casado(C) o Soltero(S):")
Lugar= input("Urbano(U) o Rural(R):")
Edad= int(2016-Año)
if ((10<Pertenencia and 2<=Hijos) or (Estado=="C" and 3<Hijos and 45<=Edad<=55) or (2500000<Ingreso and Estado=="S" and Lugar=="U") or (3500000<Ingreso and 5<Pertenencia) or (Lugar=="R" and Estado=="C" and Hijos<2)):
   print("APROBADO")
else:
   print("RECHAZADO")      
