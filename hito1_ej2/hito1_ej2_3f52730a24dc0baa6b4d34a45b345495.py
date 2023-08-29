N_str= str(input("Ingresa el número de 8 cifras de la llamada entrante:"))
print()
while len(N_str) >8:
  print("No existen números de teléfono con más de 8 cifras")
  print()
  N_str= str(input("Ingresa el número de 8 cifras de la llamada entrante:"))
  print()
N=int(N_str)    
H= float(input("Ingresa la hora a la que se efectuó la llamada:"))
print()
while True:
  if 0<=H<=7:
    print()
    print("CONTESTAR")
    print()
  elif N%1000==909:
    print()
    print("CONTESTAR")
    print()
  elif 7<H<14:
    print()
    print("NO CONTESTAR")
    print()
  elif 14<=H<17:
    print()
    print("NO CONTESTAR")
    print()
  elif N//100000==877:
    print()
    print("NO CONTESTAR")
    print()
  elif 17<=H<=19:
    print()
    print("CONTESTAR")
    print()
  elif 19<H<=23.59:
    print()
    print("NO CONTESTAR")
    print()
  break
