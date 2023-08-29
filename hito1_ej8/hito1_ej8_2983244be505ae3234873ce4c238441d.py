#Descomponer un número
nro=str(input("ingrese numero(hasta 4 digitos): "))
largo=len(nro)
if largo==4:
  print(nro[0],"M","+",nro[1],"C","+",nro[2],"D","+",nro[3],"U")
if largo==3:
  print(nro[0],"C","+",nro[1],"D","+",nro[2],"U")
if largo==2:
  print(nro[0],"D","+",nro[1],"U")
if largo==1:
  print(nro[0],"U")