#Aprobación de créditos
i=float(input("Coloque su Ingreso en pesos "))
ano=int(input("Ingrese su año de nacimiento "))
anos=2022-ano
hijos=int(input("Ingrese su número de hijos "))
apb=float(input("Ingrese sus años de pertenencia al banco "))
ec=input("Ingrese su estado civil ( S para soltero y C para casado) ")
hogar=input("Ingrese si vive en campo o ciudad ( U para zona urbana, R para zona rural) ")
if(apb>=10 and hijos>=2):
    print("APROBADO")
else:
    if(ec=="C" and hijos>3 and anos>=45 and anos<=55):
        print("APROBADO")
    else:
        if(i>2500000 and ec=="S" and hogar=="U"):
            print("APROBADO")
        else:
            if(i>3500000 and apb>5):
                print("APROBADO")
            else:
                if(hogar=="R" and ec=="C" and hijos<2):
                    print("APROBADO")
                else:
                    print("NO APROBADO")
