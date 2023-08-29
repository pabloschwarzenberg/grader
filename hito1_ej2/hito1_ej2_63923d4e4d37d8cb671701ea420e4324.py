#Contestador de celular

import string

Val_Telefono = int
Val_Hora= int
Val_Mensaje= str
Val_tele= str

Val_Telefono = int(input("Ingrese numero telefonico : "))
Val_Hora = int(input("Ingrese Hora de llamado : "))
Val_tele = str(Val_Telefono)


extrae_numero = Val_tele[5:]
Val_Exc_N = int(extrae_numero)

extrae_numero_dos = Val_tele[0:3]
Val_Exc_N2 = int(extrae_numero_dos)


if Val_Hora >= 0 and Val_Hora <= 7:
    Val_Mensaje="CONTESTAR"

elif Val_Hora < 14 and Val_Exc_N != 909:
    Val_Mensaje = "NO CONTESTAR"

elif Val_Hora < 14 and Val_Exc_N == 909:
    Val_Mensaje = "CONTESTAR"

elif Val_Hora >= 17 and Val_Hora <= 19 and Val_Exc_N2 != 877:
    Val_Mensaje = " CONTESTAR"

elif Val_Hora >= 17 and Val_Hora <= 19 and Val_Exc_N2 == 877:
    Val_Mensaje = "NO CONTESTAR"
    
elif Val_Hora > 19:
    Val_Mensaje = " NO CONTESTAR"


print("Resultado : ", Val_Mensaje)
      