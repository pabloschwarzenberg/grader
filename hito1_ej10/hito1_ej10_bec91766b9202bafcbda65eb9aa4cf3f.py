#Cajero Automático
#Recopilacion de datos

saldo_inicial = 1000000
num_usuario = 10334151
clave = 1803
usuario_dinero = 100000

user_ingresado = int(input('Ingrese su numero de usuario: '))
if user_ingresado == num_usuario:
  clave_ingresada = int(input('Ingrese la clave de usuario: '))
  if clave_ingresada == clave:
  print('Clave correcta')
elif user_ingresado != num_usuario:
  print('Numero de usuario incorrecto')
