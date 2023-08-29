#Aprobación de créditos
x1 = int(input("ingrese su ingreso en pesos: "))
x2 = int(input("ingrese su año de nacimiento: "))
x3 = int(input("ingrese el numero de hijos que tiene: "))
x4 = int(input("ingrese sus años de pertenecia al banco: "))
x5 = input("ingrese su estado civil de tal manera que S es soltero y C es casado: ")
x6 = input("ingrese si vive en campo o ciudad de manera que U es urbano y R es rural: ")
e = int(2020)-int(x2)
C = x5
S = x5
U = x6
R = x6
if x4>10 and x3>=2:
    print("APROBADO")
else:
    if x5==C and x3>3 and 45<= e <=55:
        print("APROBADO")
    else:
        if x1>=250000 and x5==S and x6==U:
            print("APROBADO")
        else:
            if x1>=350000 and x4>=5:
                print("APROBADO")
            else:
                if x6==R and x5==C and x3<2:
                    print("APROBADO")
                else:
                    print("RECHAZADO")