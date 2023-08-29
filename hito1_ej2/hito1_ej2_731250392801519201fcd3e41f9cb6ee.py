#Contestador de celular
n=int(input("numero:"))
h=int(input("hora:"))
if h >=0 and h <=7:
    print("CONTESTAR")
elif h < 14 and n%1000==909:
     print("CONTESTAR")
else:
     print("NO CONTESTAR")
     
if h >= 17 and h <= 19 and (n//100000)!= 877:
   print(" NO CONTESTAR")
else:
     print("CONTESTAR")
     
if h> 19:
   print("NO CONTESTAR")
     

   