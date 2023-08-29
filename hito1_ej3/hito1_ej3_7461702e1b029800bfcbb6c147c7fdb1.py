#Aprobación de créditos
I=int(input('Ingrese su ingreso (en pesos): '))
N=int(input('Año de nacimiento: '))
H=int(input('Ingrese el numero de hijos:'))
A=int(input('ingrese años de pertenencia al banco'))
E=str(input('ingrese su estado civil'))
V=str(input('ingrese si vive en campo o ciudad con una U urbano y R rural'))
años=2020-N
if A>10 and H>=2:
    print('APROBADO')
    
else:
    if E==('C') and H>3 and 45<=años<=55:
        print('APROBADO')
    
    else:
        if I>2500000 and E==('S') and V==('U'):
            print('APROBADO')
    
        else:
            if I>3500000 and A>5:
                print('APROBADO')

            else:
                if V==('R') and E==('C') and H<2:
                    print('APROBADO')

                else:
                    print('RECHAZADO')