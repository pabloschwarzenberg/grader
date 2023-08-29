   ##ingrese tres numeros enteros
num1=int(input("ingrese el primer número: "))
num2=int(input("ingrese el segundo número: "))    
num3=int(input("ingrese el tercer número: "))

##ordenar de menor a mayor
if num1 <= num2 <= num3:
  print (f"{num1} {num2} {num3}\n")
elif num1 <= num3 <= num2:
  print (f"{num1} {num3} {num2}")
elif num2 <= num1 <= num3:
  print (f"{num2} {num1} {num3}\n")
elif num2 <= num3 <= num1:
  print (f"{num2} {num3} {num1}\n")
elif num3 <= num1 <= num2:
  print (f"{num3} {num1} {num2}\n")
elif num3 <= num2 <= num1:
  print (f"{num3} {num2} {num1}\n")
             