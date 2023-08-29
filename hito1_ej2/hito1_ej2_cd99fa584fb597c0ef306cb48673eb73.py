telefono = int(input("Ingrese número telefónico de 8 digitos: "))
hora = int(input("Ingrese la hora de la llamada: "))

# Aqui revisimas las condiciones para ver si python contestará o no.
def contestar(telefono, hora):
    if hora >= 0 and hora<7:
        return"Contestar"
    if hora < 14 and telefono %100 != 909:
        return"Contestar"
    if hora >= 17 and hora <19 and telefono //1000000 == 877:
        return"Contestar"
    else:
        return"No contestar"
        
con=contestar(telefono,hora)
print("Resultado",con)
        