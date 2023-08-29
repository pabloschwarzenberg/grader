N=input("Ingrese numero telefonico:")
H=int(input("Ingrese hora de la llamada:")) 
if (0 < H < 7):
  print("CONTESTAR")
else:
  if (7 < H < 14) and int(N[5:])==909:
    print("CONTESTAR")
  else:
    if (7 < H < 14) and  int(N[5:])!=909:
      print("NO CONTESTAR")
    else:
      if (17 < H < 19) and int(N[:3])!=877:
        print("CONTESTAR")
      else:
        if (17 < H < 19) and int(N[:3])==877:
          print("NO CONTESTAR")
        else:
          if (19 < H < 23):
            print("NO CONTESTAR")