n=int(input("ingrese el numero telefonico: "))
h=int(input("ingrese hora de la llamada: "))
if n>9999999 and n<100000000:
 if h>=0 and h<=7:
  print("contestar")
 else:
  if n%1000==909 and h==14:
   print("contestar")
  else:
   if n//100000==877 and h>=17 and h<=19:
    print("no contestar")
   else:
    if n//100000!=877 and h>=17 and h<=19:
     print("contestar")
    else:
     if h>=19 and h<=23:
      print("no contestar")
     else:
      print("contestar")
                
