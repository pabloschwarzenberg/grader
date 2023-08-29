dig1=int(input("ingrese numero 1  : "))
dig2=int(input("ingrese numero 2  : "))
dig3=int(input("ingrese numero 3  : "))
if(dig1<=dig2<=dig3):
  print(str(dig1)+","+str(dig2)+","+str(dig3))
elif(dig1<=dig3<=dig2):
  print(str(dig1)+","+str(dig3)+","+str(dig2))
elif(dig2<=dig1<=dig3):
  print(str(dig2)+","+str(dig1)+","+str(dig3))
elif(dig2<=dig3<=dig1):
  print(str(dig2)+","+str(dig3)+","+str(dig1))
elif(dig3<=dig1<=dig2):
  print(str(dig3)+","+str(dig1)+","+str(dig2))
elif(dig3<=dig2<=dig1):
  print(str(dig3)+","+str(dig2)+","+str(dig1))