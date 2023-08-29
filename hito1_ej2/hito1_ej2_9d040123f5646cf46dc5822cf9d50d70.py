#Contestador de celular
NumeroTelefono = int(input('Ingrese numero telefonico: '))
HoraLlamada = int(input('Ingrese hora de llamada (entre 0 y 23): '))
Resultado = ''
while len(str(NumeroTelefono)) != 8:
    NumeroTelefono = int(input('Ingrese un numero de telefono valido: '))
while HoraLlamada < 0 or HoraLlamada > 23:
    HoraLlamada = int(input('Ingrese una hora valida: '))
x = str(NumeroTelefono)
if HoraLlamada > 19:
    Resultado = 'NO CONTESTAR'
elif HoraLlamada >= 17 or HoraLlamada <= 19:
    Resultado = 'CONTESTAR'
    if x[0:3] == '877':
        Resultado = 'NO CONTESTAR'
elif HoraLlamada < 14:
    Resultado = 'NO CONTESTAR'
    if x[-3:] == '909':
        Resultado = 'CONTESTAR'
elif HoraLlamada >= 0 or HoraLlamada <= 7:
    Resultado = 'CONTESTAR'
print(Resultado)