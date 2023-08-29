#Contestador de celular
tel = int(input("Ingrese numero telefonico: "))
hora = int(input("Ingrese hora: "))
if(7>hora>0): print ("CONTESTAR")
elif(14>hora and tel%1000 == 909): print ("CONTESTAR")
elif(17<hora<19 and tel%1000 == 877): print ("NO CONTESTAR")
elif(hora>19): print ("NO CONTESTAR")
else: print ("NO CONTESTAR") 