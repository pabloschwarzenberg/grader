print("Ingrese el primer numero ")
numero1=int(input())
print("Ingrese segundo numero ")
numero2=int(input())
print("Ingrese el tercer numero ")
numero3=int(input())
if (numero1<=numero2 and numero2<=numero3):
  print("", numero1, " , ", numero2, " , ", numero3)
elif(numero2<=numero1 and numero1<=numero3):
  print("", numero2, " , ", numero1, " , ", numero3)
elif(numero3<=numero1 and numero1<=numero2):
  print("", numero3, " , ", numero1, " , ", numero2) 
elif (numero3<=numero2 and numero2<=numero1):
  print("", numero3, " , ", numero2, " , ", numero1)
elif (numero1<=numero3 and numero3<=numero2):
  print("", numero1, " , ", numero3, " , ", numero2)
elif (numero2<=numero3 and numero3<=numero1):
   print("", numero2, " , ", numero3, " , ", numero1)
else:
  print("Has ingresado numeros iguales")