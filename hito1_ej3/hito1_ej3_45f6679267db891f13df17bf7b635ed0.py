print("indique sus ingresos")
INGRESOS=int(input())
print("indique su año de nacimiento")
ANONACIMIENTO=int(input())
print("Cantidad de hijos")
CANTIDADDEHIJOS=int(input())
print("indique sus años de pertenencia al banco")
ANOSENBANCO=int(input())
print("indique su estado civil, s si es soltero y c si es casado")
ESTADOCIVIL=str(input())
print("Donde vive, indique con u si es urbano y con una r si es rural")
VIVE=str(input())

if ANOSENBANCO>10 and CANTIDADDEHIJOS>=2:
  print("APROBADO")
else:
    if ESTADOCIVIL== "C" and CANTIDADDEHIJOS>3 and 1975<anodenacimiento<1985:
        print("APROBADO")
    else:
        if INGRESOS>2500000 and ESTADOCIVIL == "S" and DONDEVIVE == "U":
            print("APROBADO")
        else:
            if INGRESOS>35000000 and ANOSENBANCO>5:
                print("APROBADO")
            else:
                if VIVE == "R" and ESTADOCIVIL == "C" and CANTIDADDEHIJOS<2:
                    print("APROBADO")
                else:
                    print("RECHAZADO")