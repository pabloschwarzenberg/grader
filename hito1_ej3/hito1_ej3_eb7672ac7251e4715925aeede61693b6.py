I=int(input("Ingresos (en pesos): "))
AN=int(input("Año de Nacimiento: "))
NH=int(input("Numero de hijos: "))
AP=int(input("Años de pertenencia: "))
EC=str(input("Estado Civil: "))
CoC=str(input("Campo o Ciudad: "))
edad=(2018-AN)
if AP>=10 and NH>=2:
    print("APROBADO")
if EC=="C" and NH>3 and 45<=edad<=55:
    print("APROBADO")                  
if I>2500000 and EC=="S" and CoC=="C":
    print("APROBADO")                                     
if I>3500000 and AP>5:
    print("APROBADO")                                      
if CoC=="R" and EC=="C" and NH<2:
    print("APROBADO")

                     