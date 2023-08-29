#Descomponer un número
Numero=input("ingrese numero con maximo 4 cifras:")
if len(Numero)==4:
  print(Numero[0],"M+",Numero[1],"C+",Numero[2],"D+",Numero[3],"U+")
elif len(Numero)==3:
  print(Numero[0],"C+",Numero[1],"D+",Numero[2],"U+")
elif len(Numero)==2:
  print(Numero[0],"D+",Numero[1],"U+")
elif len(Numero)==1:
  print(Numero[0],"U+")
