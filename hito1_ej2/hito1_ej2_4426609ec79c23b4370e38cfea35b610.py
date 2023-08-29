#Contestador de celular
print("poner datos")
t = int(input("numero ="))
h = int(input("hora ="))
ts = str(t)
if(len(ts) == 8 and (h >= 0) and (h <= 23)):
    
    if((h >= 0) and(h <= 7)):
        print("CONTESTAR")
    elif((h < 14) and (ts[5:8]=="909")):
       print("CONTESTAR")
    elif((h >= 17) and (h <= 19) and (ts[0:3]!="877")):
        print("CONTESTAR")
    else:
        print("NO CONTESTAR")
else:
    print("INGRESE BIEN LOS DATOS")  
      