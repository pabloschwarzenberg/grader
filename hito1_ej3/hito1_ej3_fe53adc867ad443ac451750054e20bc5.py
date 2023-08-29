#Aprobación de créditos
print("coloque sus ingresos")
x=int(input())
print("ingrese su año de nacimiento")
y=int(input())
print("ingrese la cantidad de hijos que tiene")
z=int(input())
print("ingrese sus años de pertenencia al banco")
w=int(input())
print("ingrese su estado civil, s si es soltero y c si es casado")
a=str(input())
print("ingrese donde vive, u si es un lugar urbano y r si es un lugar rural")
b=str(input())

if w>10 and z>=2:
  print("APROBADO")
else:
    if a == "C" and z>3 and 1975<y<1985:
        print("APROBADO")
    else:
        if x>2500000 and a == "S" and b == "U":
            print("APROBADO")
        else:
            if x>35000000 and w>5:
                print("APROBADO")
            else:
                if b == "R" and a == "C" and z<2:
                    print("APROBADO")
                else:
                    print("RECHAZADO")