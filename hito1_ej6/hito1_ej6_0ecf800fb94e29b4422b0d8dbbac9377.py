#Ordenar tres números
numero1=int(input("ingrese un numero: "))
numero2=int(input("ingrese un numero: "))
numero3=int(input("ingrese un numero: "))
if(numero1<numero2<numero3):
  print("ordenados de menor a mayor:",numero1,",",numero2,",",numero3)
if(numero2<numero3<numero1):
  print("ordenados de menor a mayor:",numero2,",",numero3,",",numero1) 
if(numero3<numero1<numero2):
  print("ordenados de menor a mayor:",numero3,",",numero1,",",numero2)
if(numero1<numero3<numero2):
  print("ordenados de menor a mayor:",numero1,",",numero3,",",numero2)  
if(numero2<numero1<numero3):
  print("ordenados de menor a mayor:",numero2,",",numero1,",",numero3)  
if(numero3<numero2<numero1):
  print("ordenados de menor a mayor:",numero3,",",numero2,",",numero1)
if(numero1<numero2==numero3):
  print("ordenados de menor a mayor:",numero1,",",numero2,",",numero3)
if(numero2<numero3==numero1):
  print("ordenados de menor a mayor:",numero2,",",numero3,",",numero1) 
if(numero3<numero1==numero2):
  print("ordenados de menor a mayor:",numero3,",",numero1,",",numero2)
if(numero1==numero3<numero2):
  print("ordenados de menor a mayor:",numero1,",",numero3,",",numero2)  
if(numero2==numero1<numero3):
  print("ordenados de menor a mayor:",numero2,",",numero1,",",numero3)
if(numero3==numero2<numero1):
  print("ordenados de menor a mayor:",numero3,",",numero2,",",numero1)