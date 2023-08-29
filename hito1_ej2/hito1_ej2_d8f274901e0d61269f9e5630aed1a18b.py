#Contestador de celular

#Ingrese numero y hora
a = str(input("Digite un número telefonico de 8 cifras: "))
x = int(input("ingrese la hora con formato del 0 al 23: "))

#Regla 1, 4, 2 y 3 respectivamente

if (x>0) and (x<7):
  print("CONTESTAR")
  
if (x<23) and (x>19):
  print("NO CONTESTAR")
  
else:  
  if (x>7) and (x<14) and (str(a[-3])== "9") and (str(a[-2])== "0") and (str(a[-3])== "9"):
    print("CONTESTAR")
  
  if (x>7) and (x<14) and (str(a[-3])!= "9") and (str(a[-2])!= "0") and (str(a[-3])!= "9"):
    print("NO CONTESTAR")
    
  if (x<19) and (x>17) and (str(a[0:1])== "8") and (str(a[1:2])== "7") and (str(a[2:3])== "7"):
    print("NO CONTESTAR")
    
  if (x<19) and (x>17) and (str(a[0:1])!= "8") and (str(a[1:2])!= "7") and (str(a[2:3])!= "7"):
    print("CONTESTAR")
    
 