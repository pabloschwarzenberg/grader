#Contestador de celular
numero= int(input("numero"))
hora= int(input("hora:"))
if hora >= 0 and hora <= 7:
   print("CONTESTAR")
if hora > 7 and hora <= 14:
   if(numero%1000)==909:
       print("CONTESTAR")
   else:
        print("NO CONTESTAR")
if hora >= 17 and hora <= 19:
    if(numero//100000)==877:
        print("NO CONTESTAR")
    else:
        print("CONTESTAR")
if hora > 19:
    print("no contestar")      