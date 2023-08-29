n=eval(input("Ingresar número telefónico: "))
h=eval(input("Ingrese hora de la llamada: "))
u3d= n%1000      
if(h>=0 and h<=7):
    print("CONTESTAR")
elif(h<14 and u3d==909):
          print("CONTESTAR")
elif(h>=17 and h<=19 and u3d==877):
          print("NO CONTESTAR")
elif(h>=19):
          print("NO CONTESTAR")
else:
          print("NO CONTESTAR")