I = int(input("ingresar su sueldo en pesos: "))
A = int(input("ingresar su el año de su nacimiento: "))
N = int(input("ingresar la cantidad de hijos: "))
B = int(input("ingresar los años que ha estado en el banco: "))
E = str(input("ingresar si esta S:soltero y/o C:casado: " ))
V = str(input("ingresar si vive U:urbano y/o R:rural: "))

ACTUALIDAD = 2021
EDA_D = ACTUALIDAD-A

if B>10 and N>=2 :

     print("APROBADO")

if str(E) == "C" and N>3 and EDA_D>45 and EDA_D<55  :
   
     print("APROBADO")
      
if (I>2500000) and str(E) == "S" and str(V) == "U" :
   
     print("APROBADO")
      
if (I>=3500000) and B>5 :
   
     print("APROBADO")
      
if str(V) == "R" and str(E) == "C" and N<2 :
   
     print("APROBADO")
      
else :
    print("RECHAZADO")
      