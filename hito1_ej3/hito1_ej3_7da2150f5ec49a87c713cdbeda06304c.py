I=float(input("Ingresa tu ingreso: "))
N=int(input("Ingresa tu año nacimiento: "))
H=int(input("Ingresa tu numero de hijos:" )) 
A=int(input("Ingresa tu años en el banco: "))
C=str("Casado")
S=str("Soltero")
R=str("Rural")
U=str("Urbano")
E=str(input("Ingresa S o C: "))
L=str(input("Ingresa U o R: "))

if A>10 and H>1:
    print("APROBADO")

else:
    if E=="C" and H>3 and 45<N<55:
     print("APROBADO")

    else:
        if I>2500000 and E=="S" and L=="U":
         print("APROBADO")

        else:
            if I>3500000 and A>5:
             print("APROBADO")

            else:
                if L=="R" and E=="C" and H<2:
                 print("APROBADO")

                else:
                    print("RECHAZADO")     
