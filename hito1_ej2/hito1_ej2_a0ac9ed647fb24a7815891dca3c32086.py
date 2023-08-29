tlf = int(input("Ingrese el número telefónico: "))
hora = int(input("Ingrese la hora: "))
tlf = str(tlf)
ntf = str(tlf[5:8])

if 0 <= hora <=7:
    print("CONSTESTAR")
if ntf == str(909) and hora <= 14:
      print("CONTESTAR")
else:
    print("NO CONTESTAR")
if 17 <= hora <= 19 and int(tlf) < 87700000 and int(tlf) > 87699999:
    print("NO CONTESTAR")
else:
    print("CONTESTAR")
    