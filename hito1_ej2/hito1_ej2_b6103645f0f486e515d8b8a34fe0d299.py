a = int(input("ingrece el numero de telefono:"))
h = int(input("ingrece la hora:"))
a = str(a)
cos = a[5:8]
al = a[0:3]
num = 909
num = str(num)
num2 = 877
num2 = str(num2)
if 0 <= h <= 7:
    print("CONTESTAR")
elif 7< h <=14:
     if a[5:8] == num:
       print("CONTESTAR")
     else:
         print("NO CONTESTAR")
elif 17<= h<= 19:
    if a[0:3] == num2:
      print("NO CONTESTAR")
    else:
      print("CONTESTAR")
elif h > 19:
  print("NO CONTESTAR")