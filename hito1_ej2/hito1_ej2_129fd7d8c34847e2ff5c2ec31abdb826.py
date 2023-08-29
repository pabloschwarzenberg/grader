#Contestador de celular
val_fono=int
val_hora=int
val_mensaje=str
val_tele=str

val_fono=int(input("ingrese numero telefonico:"))
val_hora=int(input("ingrese hora de la llamada:"))
val_tele=str(val_fono)

extrae_numero = val_tele[5:]
val_Exc_N = int(extrae_numero)

extrae_numero_dos = val_tele[0:3]
val_Exc_N2 = int(extrae_numero_dos)


if val_hora >= 0 and val_hora <= 7:
    val_mensaje="CONTESTAR"

elif val_hora < 14 and val_Exc_N != 909:
    val_mensaje = "NO CONTESTAR"

elif val_hora < 14 and val_Exc_N == 909:
    val_mensaje = "CONTESTAR"

elif val_hora >= 17 and val_hora <= 19 and val_Exc_N2 != 877:
    val_mensaje = " CONTESTAR"

elif val_hora >= 17 and val_hora <= 19 and val_Exc_N2 == 877:
    val_mensaje = "NO CONTESTAR"

elif val_hora > 19:
    val_mensaje = " NO CONTESTAR"


print("Resultado : ", val_mensaje)
