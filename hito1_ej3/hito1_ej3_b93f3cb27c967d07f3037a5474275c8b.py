#Aprobación de créditos
print("bienvenidos al banco Sukarita, ingrese sus datos, por favor para sus creditos de consumo")
x=1
anobanco=0
edad=0
ingresos=int(input("ingrese sus ingresos (en peso): $"))
Numero_hijos=int(input("ingrese numero de hijos: "))
while (x>0):
    nacimiento = int(input("Ingrese su año de nacimiento: "))
    if(1000<nacimiento and 2022>nacimiento):
        edad=(2022-nacimiento)
        while (x>0):
            Ano_em_el_banco=int(input("Ingrese su año de pertenencia al banco: "))
            if(nacimiento<Ano_em_el_banco and 2022>Ano_em_el_banco):
                anobanco=(2022-Ano_em_el_banco)
                x=0
            else:
                print("ingrese año de su año de pertenencia al banco, por favor")
    else:
        print("ingrese año de su nacimiento nuevamente, por favor")
x=1
while (x>0):
    Estado_civil=input("ingrese si es casado o soltero (S: soltero, C, casado):" )
    if(Estado_civil=="S" or Estado_civil=="C"):
        x=0
    else:
        print("Ponga una C si eres casado o S si eres Soltero, porfavor")
x=1
while (x>0):
    lugar=input("imgrese si vive en campo o cuidad (U: urbano, R: rural)")
    if(lugar=="U" or lugar=="R"):
        x=0
    else:
        print("Ponga una U si eres de la ciudad o R si eres del campo, porfavor")
if(anobanco<10 and Numero_hijos>=2):
    print("APROBADO ")
elif(Estado_civil=="C" and Numero_hijos>3 and 45<edad<55):
        print("APROBADO ")
elif(2500000<ingresos and lugar=="C" and Estado_civil=="S" ):
        print("APROBADO ")
elif(3500000<ingresos and anobanco<5):
        print("APROBADO ")
elif(lugar=="R" and Estado_civil=="C" and Numero_hijos<2):
        print("APROBADO ")
else:
        print("RECHAZADO ")
