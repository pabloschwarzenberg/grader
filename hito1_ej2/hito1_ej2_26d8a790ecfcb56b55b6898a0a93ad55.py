#Contestador de celular
numero=int(input("Ingrese su numero de 8 cifras: ", ))
hora=int(input("Ingrese su hora: ", ))
final = numero%1000
inicio = numero//100000
if hora>0 and hora <=7:
    print("CONTESTAR")
if hora>7 and hora<14:
    if final == 909:
        print("CONTESTAR")
    else:
        print("NO CONTESTAR")
if hora>=14 and hora<17:
    print("NO CONTESTAR")
if hora>=17 and hora<=19:
    if inicio == 877:
        print("NO CONTESTAR")
    else:
        print("CONTESTAR")
if hora > 19:
    print("NO CONTESTAR")
print("Los ultimos tres digitos son",final)
print("Los primeros tres digitos son",inicio)