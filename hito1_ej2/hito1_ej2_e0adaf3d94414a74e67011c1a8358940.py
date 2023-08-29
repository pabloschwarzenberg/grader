#Contestador de celular
b = int(input("Ingrese su número de celular: \n"))
a = int(input("Ingrese hora de la llamada (Entre 0 y 23 horas): \n"))
if(a>=0 and 23>=a):
  
  if(len(str(b))==8):
    if 0 >= a and a <=7:
     print("CONTESTAR")
    elif(a < 14 ): 
        if((b%1000 == 909)):
          print("CONTESTAR")
        else:
          print("NO CONTESTAR")
    elif(a>=14 and 17>a):
      print("NO CONTESTAR")
    elif(a>=17 and a<19):
      if(b//100000 ==877):
        print("NO CONTESTAR")
      else:
        print("CONTESTAR")
    elif(a>19):
      print("NO CONTESTAR")
  else:
    print("Ingrese teléfono correcto")
else:
  print("Ingrese hora correcta")