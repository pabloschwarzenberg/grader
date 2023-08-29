#Ordenar tres números
numero1=int(input("ingrese el numero 1: "))
numero2=int(input("ingrese el numero 2: "))
numero3=int(input("ingrese el numero 3: "))
if(numero1<=numero2<=numero3):
  print(str(numero1)+",",str(numero2)+",",str(numero3))
if(numero3<=numero2<=numero1):
   print(str(numero3)+",",str(numero2)+",",str(numero1))
if(numero2<=numero3<=numero1):
  print(str(numero2)+",",str(numero3)+",",str(numero1))
if(numero1<=numero3<=numero2):
  print(str(numero1)+",",str(numero3)+",",str(numero2))
if(numero2<=numero1<=numero3):
  print(str(numero2)+",",str(numero1)+",",str(numero3))
if(numero3<=numero1<=numero2):
  print(str(numero3)+",",str(numero1)+",",str(numero2))