#Descomponer un número
a= input("ingrese un número que contenga como máximo 4 digitos")
if len(a)==4:
      print(a[-4], 'M +',a[-3], 'C +',a[-2], 'D +', a[-1],'U')
if len(a)==3:
      print(a[-3], 'C +',a[-2], 'D +', a[-1],'U')
if len(a)==2:
      print(a[-2], 'D +', a[-1],'U')
if len(a)==1:
      print(a[-1],'U')