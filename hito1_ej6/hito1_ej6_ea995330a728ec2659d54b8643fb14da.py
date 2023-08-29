numero1=eval(input("Ingrese numero: "))
numero2=eval(input("Ingrese numero: "))
numero3=eval(input("Ingrese numero: "))

if(numero1>=numero2>=numero3):
  print(numero3,",",numero2,",",numero1)
if(numero3>=numero2>=numero1):
  print(numero1,",",numero2,",",numero3)
if(numero2>=numero3>=numero1):
   print(numero1,",",numero3,",",numero2)
if(numero2>=numero1>=numero3):
   print(numero3,",",numero1,",",numero2)
if(numero1>=numero3>=numero2):
  print(numero2,",",numero3,",",numero1)
if(numero3>=numero1>=numero2):
   print(numero2,",",numero1,",",numero3)