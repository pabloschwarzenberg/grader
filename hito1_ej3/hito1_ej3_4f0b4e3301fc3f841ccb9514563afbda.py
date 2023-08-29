#Aprobación de créditos
ingreso=int(input('Digite su Ingreso en pesos: '))
year=int(input('Ingrese año de nacimiento: '))
hijos=int(input('Ingrese numero hijos: '))
pertenencia=int(input('Ingrese años de pertenencia al banco: '))
estado=input('Ingrese estado civil S soltero C casado: ')
dvive=input('Donde vive? U urbano. R rural: ')

if pertenencia >= 10 and hijos >= 3:
        print('APROBADO')
        
else:
    if estado== 'C' and hijos >= 3 and 1975 >= year <= 1965:
     print('APROBADO')
    else:
        if ingreso>=2500000 and estado=='S' and dvive=='U':
            print('APROBADO')
        else:
            if ingreso>=2500000 and pertenencia >= 5:
                print('APROBADO')
            else:   
                if dvive=='R' and estado=='C' and hijos < 2:
                   print('APROBADO')
                else:
                    print('RECHAZADO')

            
