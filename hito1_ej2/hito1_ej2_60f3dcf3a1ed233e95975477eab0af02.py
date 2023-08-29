#Contestador de celular
#numero 
n2 = int(input("numero telefonico: "))
n1 = str(n2)
n = n1[0:8] 
#hora de llamada
h3 = int(input("hora de llamada: "))
23>=h3>0
h2 = str(h3)
h1 = h2[0:2]
h = int(h1)
#condiciones
if 7>=h>=0:
  print ("contestar")
elif  14>h>=7 and n[5:8]=="909":
  print ("contestar")
elif 14>h>=7:
  print ("no contestar")
elif 17>h>=14:
  print ("no contestar")
elif 19>=h>=17 and n[0:3]=="877":
  print("no contestar")
elif 19>=h>=17:
  print ("contestar")
else:
  print ("no contestar")