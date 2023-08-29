#Aprobación de créditos
print("ingreso en pesos")
ingresos=float(input())
print("año nacimineto")
nacimineto=int(input())
print("numero de hijos")
hijos=int(input())
print("añoes de permanencia en banco")
tiempoenbanco=int(input())
print("Estado Civil: C (casado) o S (solero)")
estado=str(input())
print("donde vive : U (ciudad) o R (campo)")
hogar=str(input())
edad= 2016-nacimineto

if( tiempoenbanco>=10 and hijos>=2):
    print("APROBADO")
else:
    if( estado=="S" and hijos>=3 and 45<=edad>=55):
        print("APROBADO")
    else:
        if( ingresos>2500000 and estado=="S" and hogar=="U"):
            print("APROBADO")

        else:
            if( ingresos>3500000 and tiempoenbanco>5):
                print("APROBADO")

            else:
                if( hogar=="R" and estado =="C" and hijos<2):
                    print("APROBADO")
                else:
                    print("RECHAZADO")