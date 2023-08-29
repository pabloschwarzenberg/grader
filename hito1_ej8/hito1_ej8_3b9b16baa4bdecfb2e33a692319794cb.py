#Descomponer un número
numero=int(input())
numero_=str(numero)
if len(numero_)==4:
  print(numero_[0],"M+",numero_[1],"C+",numero_[2],"D+",numero_[3],"U+")
elif len(numero_)==3:
  print(numero_[0],"C+",numero_[1],"D+",numero_[2],"U+")
elif len(numero_)==2:
  print(numero_[0],"D+",numero[1],"U+")
elif len(numero_)==1:
  print(numero_[0],"U+")