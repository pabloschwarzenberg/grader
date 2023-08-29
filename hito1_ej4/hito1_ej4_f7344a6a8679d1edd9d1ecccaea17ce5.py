def decimal_a_binario(dec):
    if dec <= 0:
        return "0"
    bina = ""
    while dec > 0:
        residuo = int(dec % 2)
        dec = int(dec / 2)
        bina = str(residuo) + bina
    return bina
dec = int(input("Ingresa un n decimal: "))
bina = decimal_a_binario(dec)
print( "resultado=",(bina) )
      