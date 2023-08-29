#Contestador de celular
t=(input("Ingrese su telefono de ocho digitos: "))
h=int(input("Ingrese hora: "))

if h>=0 and h<=7 or h<14 and t[5:8]=="909" or h>=17 and h<=19 and t[0:3]!="877":
   print("Contestar")
   
else:
    print ("No Contestar")
     