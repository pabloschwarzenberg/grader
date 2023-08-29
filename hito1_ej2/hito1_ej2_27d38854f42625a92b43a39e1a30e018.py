#Contestador de celular
 
n=input("TELEFONO")
b=int(input("Hora"))
 
if b<=7:
   print("CONTESTAR")
 
if b>7 and b<14:
   if n[5]=='9' and n[6]=='0' and n[7]=='9':
     print("CONTESTAR")
   else:
     print("NO CONTESTAR")
if b>=17 and b<=19:
   if n[0]=='8' and n[1]=='7' and n[2]=='7':
      print("NO CONTESTAR")
   else:
      print("CONTESTAR")
      
if b>19:
   print("NO CONTESTAR")