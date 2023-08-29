#Contestador de celular
nt= int(input('ingrese su numero telefonnico: '))
hr= int(input('ingrese hora de la llamada: '))

if hr<0 or hr>23:
    print('porfavor ingrese una hora valida')
else:
    q1= nt*(10**-8)
    q2= int(q1)
    if q2 != 0:
        print('porfavor ingresar un numero telefonico  de 8 digitos')
    else:
        if hr> 0 and hr< 7:
            print('CONTESTAR')

        elif hr> 7 and hr< 14:
             p1=nt*(10**-3)
             p2=int(p1)
             p3=p1-p2
             p4=round(p3,3)
             p5=p4*(10**3)
             nt1=int(p5)
             if nt1 == 909:
                 print('CONTESTAR')
             else:
                 print('NO CONTESTAR')
                 
        elif hr>=14 and hr<17:
            print('NO CONTESTAR')

        elif hr>=17 and hr<19:
            p1=nt*(10**-5)
            nt1=int(p1)
            if nt1 == 877:
                print('NO CONTESTAR')
            else:
                print('CONTESTAR')
                
        elif hr>19:
            print('NO CONTESTAR')