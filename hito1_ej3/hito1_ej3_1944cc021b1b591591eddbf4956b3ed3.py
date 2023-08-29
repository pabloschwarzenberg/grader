#Aprobación de créditos
ingreso = int(input('Ingrese que ingresos posee: '))
año = int(input('Ingrese su año de nacimiento: '))
hijos = int(input('Ingrese su cantidad de hijos: '))
banco = int(input('Ingrese año de pertenencia al banco: '))
ecivil = (input('Ingrese su estado civil S/C: '))
vive = (input('Ingrese donde reside U/R: '))

C = "casado"
S = "soltero"
U = "urbano"
R = "rural"

edad = año - 2023


if banco >= 10 and hijos >= 2:
    print('APROBADO')

elif ecivil == "casado" and hijos >= 3 and edad >= 45 and edad <= 55:
    print('APROBADO')
    
elif ingreso >= 250000 and ecivil == S and vive == "urbano":
        print('APROBADO')
        
elif ingreso >= 350000 and banco >= 5:
        print('APROBADO')
        
elif vive == "rural" and ecivil == "casado" and hijos <= 2:
        print('APROBADO')
else:
    print('RECHAZADO')