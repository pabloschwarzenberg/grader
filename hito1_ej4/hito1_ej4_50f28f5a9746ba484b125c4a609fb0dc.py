from os import system
system("cls")
print("Ingrese un numero decimal:")
dec=input()
if dec.isdigit:
    dec1=int(dec)
    dec2=bin(dec1)
    dec3=dec2.replace("b","")
    dec4=dec3.replace('0',  '', 1)
    print("Resultado=", dec4)
else:
    print("Error en el dato")