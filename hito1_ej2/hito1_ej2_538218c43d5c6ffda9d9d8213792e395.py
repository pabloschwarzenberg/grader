print('Aviso: Nro telefonico sin signos y sin espacios, la hora entre 0 hrs y 23 hrs')
t=int(input('digite el numero telefonico de ocho cifras: '))
h=int(input('Digite la hora de llamada: '))
T= t%10**3
C=t//10**5
if h<0 or 23<h:
    print('No digitaste una hora valida')
if t>99999999 or t<=9999999:
    print('Numero telefonico no valido')
elif 0<=h<7:
    print('Contestar')
elif 7<=h<=14 and T==909:
    print('Contestar')
elif 7<=h<=14:
    print('No contestar')
elif 14<h<17:
    print('No contestar')
elif 17<=h<=19 and C==877:
    print('No contestar')
elif 17<=h<=19:
    print('Contestar')
elif 19<h<=23:
    print('No contestar') 