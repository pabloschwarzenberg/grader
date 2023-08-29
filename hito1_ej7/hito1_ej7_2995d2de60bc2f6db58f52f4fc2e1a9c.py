#Zodiaco
dia=int(input('escribe tu dia de nacimiento:'))
mes=int(input('escribe mes de nacimiento:'))
if mes==marzo and dia>=21 or mes==abril and dia<=19:
print('aries')
elif mes==marzo and dia<21 or mes==febrero and dia>18:
print'picis')
elif mes==abril and dia>19 or mes==mayo and dia<21:
print('tauro')
elif mes==mayo and dia>20 or mes==junio and dia<22:
print('geminis')
elif mes==junio and dia>21 or mes==julio and dia<23:
print('cancer')
elif mes==julio and dia>22 or mes==agosto and dia<23:
print('leo')
elif mes==agosto and dia>22 or mes==septiembre and dia<23:
print('virgo')
elif mes==septiembre and dia>22 or mes==octubre and dia<23:
print('libra')
elif mes==octubre and dia>22 or mes==noviembre and dia<23:
print('escorpion')
elif mes==noviembre and dia>22 or mes==diciembre and dia<22:
print('sagitario')
elif mes==diciembre and dia>21 or mes==enero and dia<21:
print'(capricornio')
elif mes==enero and dia>20 or mes==febrero and dia<19:
print('acuario')
else:
print('no entra')

