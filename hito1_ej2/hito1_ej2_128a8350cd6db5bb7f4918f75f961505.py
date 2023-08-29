#Contestador de celular
numero= int(input("escribe un numero de 8 cifras: "))
hora= int(input("ingrese la hora: "))
if 7>=hora>=0:
      print("CONTESTAR")
elif 14>=hora>=8 and numero==77389909:
   print("CONTESTAR")
elif 14>=hora>=8:
    print("NO CONTESTAR")
elif 19>=hora>=17 and numero==87765545:
        print("NO CONTESTAR")
elif 19>=hora>=17:
           print("CONTESTAR")
else:
      print("NO CONTESTAR")

