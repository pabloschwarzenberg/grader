numero=input("Ingrese numero de 4 cifras: ")
if(len(numero)==4):
 print("{}M + {}C + {}D + {}U".format(numero[0],numero[1],numero[2],numero[3]))
if(len(numero)==3):
  print("{}C + {}D + {}U".format(numero[0],numero[1],numero[2]))
if(len(numero)==2):
 print("{}D + {}U".format(numero[0],numero[1]))
if(len(numero)==1):
  print("{}U".format(numero[0]))
