#Contestador de celular
numero=input("ingrese numero:")
hora=int(input("ingrse hora:"))
if hora >= 0 and hora<= 7:
    print("CONTESTAR")
elif hora >= 8 and hora < 14 and (int(numero[5] + numero[6] + numero[7]) == 909):
    print("CONTESTAR")

elif hora >= 17 and hora < 19:
    if (int(numero[0] + numero[1] + numero[2]) == 877):
        print("NO CONTESTAR")
    else:print("CONTESTAR")
elif hora > 19:
    print("NO CONTESTAR")
else:"NO CONTESTAR"
      