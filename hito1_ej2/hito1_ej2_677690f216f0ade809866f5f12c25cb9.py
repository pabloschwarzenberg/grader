#Contestador de celular
numeroTelefono = int(input("Ingrese su numero de telefono(8 digitos): "))  #int 8 cifras
horaLlamada = int(input("Ingrese la hora de llamada(entre 0 y 23): "))     #int entre 0 y 23
ultimasTresCifras = numeroTelefono %1000
primerasTresCifras = numeroTelefono // 100000
if ((numeroTelefono // 100000000) != 0):
    print("Numero invalido.")
    if(horaLlamada > 23 or horaLlamada < 0):
        print("Hora invalida.")



#Si la llamada ocurre entre 00:00 y 07:00 CONSTESTAR
if horaLlamada >= 0 and horaLlamada <= 7:
    print("CONTESTAR.")
# entre 8 y 14 NO CONTESTAR, EXCEPTO SI 3 ULTIMAS CIFRAS SON 909
if horaLlamada >= 8 and horaLlamada <= 14:
    if ultimasTresCifras == 909:
        print("CONTESTAR.")
    else:
        print("NO CONTESTAR.")
#Entre 17 y 19 CONTESTAR, MENOS 877 PRIMERAS 3 CIFRAS
if horaLlamada >= 17 and horaLlamada <= 19:
    if primerasTresCifras == 877:
        print("NO CONTESTAR.")
    else:
        print("CONTESTAR.")
# MAYOR A 19 NO CONTESTAR  
if horaLlamada > 19:
    print(" NO CONTESTAR.")