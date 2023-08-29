no=int(input("Ingrese el numero que llama: "))
hr=int(input("Ingrese la hora de llamada: "))
un=(no%1000)  #3 ultimos numeros
pn=(no//100000)  #3 numero
if hr<19:
  if (hr>=0) & (hr<=7):
    print("CONTESTAR")
  else:
    if (hr>7) & (hr<14):
      if (un==909):
        print("CONTESTAR")
      else:
        print("NO CONTESTAR")
    else:
      if (hr>13) and (hr<17):
        print("CONTESTAR")
      else:
        if(hr>17):
          if(pn==877):
            print("NO CONTESTAR")
          else:
            print("CONTESTAR")
else:
  print("NO CONTESTAR")
