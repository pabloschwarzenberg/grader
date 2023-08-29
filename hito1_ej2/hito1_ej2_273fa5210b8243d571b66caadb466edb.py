#Contestador de celular
n=int(input("Ingrese número telefónico: "))  
if not(10000000<n<100000000):
  print("El número debe tener 8 cifras.")
else:
  t=int(input("Ingrese hora de la llamada: "))
  if not(0<=t<=23):
    print("La hora de llamada debe estar entre 0 y 23.")
  else:
    if(t<=7):
      print("CONTESTAR")
#Contestar antes de 14 a 909
    elif(7<t<14) and (n%1000==909):
      print("CONTESTAR")
#Contestar solo entre 17-19 NO a 877
    elif(17<=t<=19):
      if(n//100000==877):
        print("NO CONTESTAR")
      else:
        print("CONTESTAR")
    else:
      print("NO CONTESTAR")
      
  