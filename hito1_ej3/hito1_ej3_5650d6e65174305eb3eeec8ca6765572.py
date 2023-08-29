print('Hola, ingrese los siguientes datos:')
dinero=int(input('Sus ingresos:$'))
edad=int(input('Año de nacimiento:'))
hijos=int(input('Número de hijos:'))
banco=int(input('Años de pertenencia al banco:'))
estado=str(input('Estado cívil ("S": soltero, "C", casado):'))
vida=str(input('Lugaro donde vive("U": urbano, "R": rural):'))





if banco>10 and 2<=hijos:
    print('APROBADO')

elif estado=='C' and hijos>3 and 45<=2020-edad<=55 :
    print('APROBADO')
    
elif dinero>2500000 and estado=='S'  and vida=='U':
    print('APROBADO')

elif dinero>3500000 and banco>5:
    print('APROBADO')

elif vida=='R' and estado=='C' and hijos<2:
    print('APROBADO')
else:
    print('RECHAZADO')

        
