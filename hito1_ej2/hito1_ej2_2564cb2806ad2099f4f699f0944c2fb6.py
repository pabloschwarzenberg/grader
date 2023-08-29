#Contestador de celular
a=input("Ingrese número telefónico de 8 cifras:")
b=int(input("Ingrese hora de la llamada:"))
if(0<=b<=23):
    if(0<=b<=7):print("CONTESTAR")
    else:
        if(7<b<=14):
            if(int(a[5:])==909):print("CONTESTAR")
            else:print("NO CONTESTAR")
        else:
            if(14<b<17):print("NO CONTESTAR")
            else:        
                 if(17<=b<=19):
                   if(int(a[0:3])==877):print("NO CONTESTAR")
                   else:print("CONTESTAR")
                 else:
                     if(19<b<=23):print("NO CONTESTAR")
else: print("Número telefónico inválido")
            
      