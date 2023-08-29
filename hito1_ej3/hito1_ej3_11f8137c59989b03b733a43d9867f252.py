#Aprobación de créditos
print('Bienvenido, para  la aprobación de su crédito es necesario que revisemos que cumpla con los requisitos, a través de los datos que nos entregue a continuación.')
dinero=int(input('¿Qué cantidad de dinero (en pesos) desea ingresar?: '))
año1 = int(input('¿Cuál es su año de nacimiento?: '))
hijos=int(input('¿Cuántos hijos tiene?: '))
año2=int(input('¿Por cuántos años ha pertenecido al banco?: '))    
estadocivil=input('¿Cuál es su estado civil?(Responda "S" si es soltero y "C" si es casado): ')
lugar=input('Si vive en campo coloque una "R", y si vive en ciudad una "U": ')
print('Muchas gracias por sus respuestas, el resultado de su crédito es:')
if  (año2>10 and hijos>=2)or(estadocivil=="C" and hijos>3 and 1961<=año1<=1971)or(dinero>2500000 and estadocivil=="S" and lugar=="U")or(dinero>3500000 and año2>5)or(lugar=="R" and estadocivil=="C" and hijos<2):
    print('APROBADO')
else:
    print('RECHAZADO')      