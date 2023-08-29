n=int(input("ingrese su numro de telefono"))
h=int(input("ingrese hora de llamada"))
m=round((n/100000))
if 7>=h>=0 :
      print("CONTESTAR")
elif 14>h>7 and n%1000==909 :
      print("CONTESTAR")
elif h>19 :
    print("NO CONTESTAR")
elif 17>h>=14 :
      print("NO CONTESTAR")
elif 19>= h>=17 and m!= 878 and m!=878 :
      print("CONTESTAR")
else :
      print("NO CONTESTAR")
      