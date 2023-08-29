a=input("Ingrese número telefónico:")
b=input("Ingrese hora de llamada:")
if b>="0" and b<"7":
   print("CONTESTAR")
if b>="7" and b<"14":
   if a%1000==909:
      print("CONTESTAR")
   else: 
      print("NO CONTESTAR")
if b>="17" and b<="19":
   if a>="87700000" and a<="87799999":
      print("NO CONTESTAR")
   else: 
      print("CONTESTAR")
if b>="19" and b<"23":
   print("NO CONTESTAR")
   
   