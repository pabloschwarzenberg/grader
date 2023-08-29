#Aprobación de créditos
x=int(input("ingrese cuanto ingresara"))
y=int(input("ingrese su año de nacimiento"))
z=int(input("ingrese la cantidad de hijos"))
w=int(input("cuantos años lleva en el banco"))
a=str(input("ingrese estado vicil, si si es soltero o c si es casado"))
b=str(input("ingrese donde vive, u si es lugar urbano o r si es rural"))

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
