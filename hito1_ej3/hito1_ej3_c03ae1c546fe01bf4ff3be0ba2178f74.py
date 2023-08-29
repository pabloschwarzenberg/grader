#Aprobación de créditos
I=int(input("Ingrese el monto disponible en el banco: "))
A=int(input("Ingrese su año de nacimiento: "))
N=int(input("Ingrese el número de hijos: "))
P=int(input("Ingrese los años de pertenencia al banco: "))
E=str(input("Digite S si está soltero o C si está casado: "))
V=str(input("Digite U si vive en ciudad o R si vive en el campo: "))
if P >= 10 and N >= 2:
    print("APROBADO")
else:
    if E == "C" and N >= 3 and 45 <= 2017-A and 2017-A >= 55:
        print("APROBADO")
    else:
        if I >= 2500000 and E == "S" and V == "U":
            print("APROBADO")
        else:
            if I >= 3500000 and P >= 5:
                print("APROBADO")
            else:
                if V == "R" and E == "C" and -1 < N < 2:
                    print("APROBADO")
                else:
                    print("RECHAZADO")
                    
        
                
              
