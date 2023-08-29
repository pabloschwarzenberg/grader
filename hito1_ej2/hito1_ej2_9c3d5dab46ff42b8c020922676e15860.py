#Contestador de celular
Numero = int(input("ingrese el numero de telefono de 8 digitos : "))
HoraLLamada = int(input("ingrese la hora de la llamada que se realiza entre las 0 y las 23 : "))
UltimoNumero = Numero%1000
PrimerNumero = Numero//100000

if HoraLLamada<=0 and HoraLLamada<=7:
    print("contestar por emergencia")
else:
    if HoraLLamada>7 and HoraLLamada<14 and UltimoNumero ==909:
       print("contestar")
    else:
        if HoraLLamada>7 and HoraLLamada<14:
           print("no contestar")
        else:
           if HoraLLamada>17 and HoraLLamada<19 and PrimerNumero ==877:
              print("no contestar")
           else:
              if HoraLLamada>17 and HoraLLamada<19:
                 print("contestar")
              else:
                  if HoraLLamada>19:
                     print("no contestar")