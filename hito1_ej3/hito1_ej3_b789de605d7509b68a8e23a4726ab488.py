'''Un Banco desea implementar una política de atención automatizada de créditos de consumo, y te contrata para programar su servicio. Los postulantes entregarán al banco la siguiente información:

Ingreso (en pesos)
Año de nacimiento
Número de hijos
Años de pertenencia al banco
Estado civil ("S": soltero, "C", casado)
Si vive en campo o cuidad ("U": urbano, "R": rural)

El banco usará las siguientes reglas para decidir la aprobación del crédito, con una de ellas que se cumpla, se aprueba el crédito:

Si el cliente pertenece más de 10 años al banco, y tiene dos o más hijos.
Si el cliente es casado, tiene más de tres hijos, y tiene entre 45 y 55 años.
Si el cliente posee ingresos superiores a $2.500.000, es soltero y vive en la ciudad.
Si el ciente tiene ingresos superiores a $3.500.000 y pertenece al banco por más de 5 años
Si el cliente vive en el campo, es casado y tiene menos de dos hijos.
Tu programa debe preguntar sus datos al cliente, procesarlos, e imprimir el mensaje APROBADO o RECHAZADO según corresponda.'''

msj1='Ingreso (en pesos):\t'
msj2='Año de nacimiento:\t'
msj3='Número de hijos:\t'
msj4='Años de pertenencia al banco:\t'
msj5='Estado civil ("S": soltero, "C", casado):\t'
msj6='Si vive en campo o cuidad ("U": urbano, "R": rural):\t'
informacion=[input(msj1),input(msj2),input(msj3),input(msj4),input(msj5),input(msj6)]
print(informacion)
E0=informacion[0].isalnum()
E1=(int(informacion[3])>10)and(int(informacion[2])>=2)
E2=(informacion[4].isupper()=='C') and (int(informacion[2])>3) and (55>=(2022-int(informacion[1]>=45)))
E3=(int(informacion[0])>2500000)and(informacion[4].isupper()=='S')and(informacion[5].isupper()=='U')
E4=(int(informacion[0])>3500000)and(int(informacion[3]>5))
E5=(informacion[5].isupper()=='R')and(informacion[4].isupper()=='C')and(int(informacion[2]<2))
while E0 is True:
    if (E0 or E1 or E2 or E3 or E4 or E5) is True:
        print('APROBADO')
        break
    else:
        print('RECHAZADO')
        break
print('Informacion Erronea Intente denuevo.\n')