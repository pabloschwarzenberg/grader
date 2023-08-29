#Contestador de celular
numero_cel=int(input("Ingresar número telefónico: "))
hora_llamada=int(input("Ingresar hora de llamada: "))
antes_14=numero_cel % 10**3
antes_17_19=numero_cel // 10**5
if hora_llamada>=19: 
   print ("No contestar.")
if hora_llamada>=0 and hora_llamada<=7 and antes_14!=909: 
   print ("Contestar.")
if hora_llamada<14 and antes_14==909: 
   print ("Contestar.")
if hora_llamada>=17 and hora_llamada<=19 and antes_17_19==877: 
   print ("No contestar.")