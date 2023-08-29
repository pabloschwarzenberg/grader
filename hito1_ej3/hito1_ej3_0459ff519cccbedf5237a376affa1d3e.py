#Aprobación de créditos
print("indique sus ingresos")
INGRESOS=int(input())
print("indique su año de nacimiento")
ANONACIMIENTO=int(input())
print("indique la cantidad de hijos que tiene")
CANTIDADDEHIJOS=int(input())
print("indique sus años de pertenencia al banco")
ANOSENBANCO=int(input())
print("indique su estado civil, s si es soltero y c si es casado")
ESTADOCIVIL=str(input())
print("indique donde vive, u si es un lugar urbano y r si es un lugar rural")
DONDEVIVE=str(input())

if ANOSENBANCO>10 and CANTIDADDEHIJOS>=2:
  print("APROBADO")
else:
    if ESTADOCIVIL== "C" and CANTIDADDEHIJOS>3 and 1975<ANONACIMIENTO<1985:
        print("APROBADO")
    else:
        if INGRESOS>2500000 and ESTADOCIVIL == "S" and DONDEVIVE == "U":
            print("APROBADO")
        else:
            if INGRESOS>35000000 and ANOSENBANCO>5:
                print("APROBADO")
            else:
                if DONDEVIVE == "R" and ESTADOCIVIL == "C" and CANTIDADDEHIJOS<2:
                    print("APROBADO")
                else:
                    print("RECHAZADO")