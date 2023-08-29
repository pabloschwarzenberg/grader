#Ordenar tres números
numero1 = eval(input("ingrese un numero"))
numero2 = eval(input("ingrese un numero"))
numero3 = eval(input("ingrese un numero"))
#odenar los numeros segun su valor
if(numero1 <= numero2 and numero2 <= numero3):
  print(eval("numero1, numero2, numero3"))
if(numero1 <= numero3 and numero3 <= numero2):
   print(eval("numero1, numero3, numero2")) 
if(numero2 <= numero1 and numero1 <= numero3):
  print(eval("numero2, numero1, numero3"))
if(numero2 <= numero3 and numero3 <= numero1):
  print(eval("numero2, numero3, numero1"))    
if(numero3 <= numero1 and numero1 <= numero2):
  print(eval("numero3, numero1, numero2")) 
if(numero3 <= numero2 and numero2 <= numero1):
  print(eval("numero3, numero2, numero1"))  