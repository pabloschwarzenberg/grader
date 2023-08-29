#Contestador de celular
telefono=str(input("Numero del contacto:"))
L=int(input("Hora de la llamada:"))
if L>19 and L<= 23:
    print("NO CONTESTAR")
elif L>0 and L<7:
    print("CONTESTAR")
else:
    if L > 7 and L < 14 and str(telefono[-3]) != "9" and str(telefono[-2]) != "0" and str(telefono[-1]) != "9":
        print("NO CONTESTAR")
    if L > 7 and L < 14 and str(telefono[-3]) == "9" and str(telefono[-2]) == "0" and str(telefono[-1]) == "9":
        print("CONTESTAR")
    if L > 17 and L < 19 and str(telefono[0:1]) != "8" and str(telefono[1:2]) != "7" and str(telefono[2:3]) != "7":
        print("CONTESTAR")
    if L > 17 and L < 19 and str(telefono[0:1]) == "8" and str(telefono[1:2]) == "7" and str(telefono[2:3]) == "7":
        print("NO CONTESTAR")