a=int(input("ingrese número de télefono:"))
b=int(input("ingrese hora del llamado:"))

if 0<=b<=7:
  print("CONTESTAR")

elif 7<b<14 and a%1000==909:
  print("CONTESTAR")
elif 17<b<19 and ((a//100000)!=877):
  print("CONTESTAR")
else:
  print("NO CONTESTAR")
      
      