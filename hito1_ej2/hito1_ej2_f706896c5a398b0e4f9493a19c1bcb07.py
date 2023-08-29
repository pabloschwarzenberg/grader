#Contestador de celular
a=(input("Numero telefonico= "))
b=int(input("Hora de llamada= "))
if b>=0 and b<=7 :
    print("CONTESTAR")
elif b>19 :
    print("NO CONTESTAR")
elif b<14 and a[-3:]=="909" :
    print("CONTESTAR")
elif b<14 and a[-3:]!="909" :
    print("NO CONTESTAR")
elif (b>=17 and b<=19) and a[0:3]=="877" :
    print("NO CONTESTAR")
elif (b>=17 and b<=19) and a[0:3]!="877" :
    print("CONTESTAR")
