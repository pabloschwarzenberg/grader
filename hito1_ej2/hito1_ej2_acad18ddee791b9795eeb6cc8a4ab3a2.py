#Contestador de celular
a=(input("Ingrese su número de telefono:"))
b=int(input("Ingrese hora:"))
if(0<=b<=23):
    if(0<=b<=7):print("CONTESTAR")
    else:
        if(7<b<=14):
            if(int(a[-3:])!=909):print("NO CONTESTAR")
            else: print("CONTESTAR")
        else:
            if(14<b<=19):
                if(17<=b<=19): 
                  if(int(a[:3])== 877): print("NO CONTESTAR")
                  else: print ("CONTESTAR")
                else: print("NO CONTESTAR")     
            else:
                if(19<b):print("NO CONTESTAR")
else: print("ingrese solo 8 numeros")
                   