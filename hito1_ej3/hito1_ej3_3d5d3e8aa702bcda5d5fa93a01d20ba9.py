#Aprobación de créditos
Añopresente=print("estamos a 2018")


ingresos=int(input("¿Cuál es su ingreso(en pesos)?: "))
Año=int(input("Ingrese su año de nacimiento: "))
Hijos=int(input("¿Cuántos hijos tiene?: "))
Banco=int(input("Ingrese sus años de pertenencia en nuestro banco: "))
EC=input("¿Cuál es su estado civil?, responda con una (C) si es casado y con una (S) si es soltero: ")
Resid=input("¿vive en un espacio rural o urbano?, responda (R) si es rural o (U) si es urbano: ")
 
if Año>10 and Hijos>2:
    print("APROBADO")
else:
    print("RECHAZADO")
    
if EC=="C" and Hijos>3 and 1963<=Año<=1973:
    print("APROBADO")
else:
    print("RECHAZADO")
               
if ingresos>2500000 and EC=="S" and Resid=="U":
    print("APROBADO")
else:
    print("RECHAZADO")
              
if ingresos>3500000 and Banco>5:
    print("APROBADO")
else:
    print("RECHAZADO")
              
if Resid=="R" and EC=="C" and Hijos<2:
    print("APROBADO")
else:
    print("RECHAZADO")
               