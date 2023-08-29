#Aprobación de créditos
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