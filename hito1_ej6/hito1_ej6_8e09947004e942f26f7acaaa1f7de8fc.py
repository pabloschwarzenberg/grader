#Ordenar tres números
numero1 = eval(input("ingrese un numero"))
numero2 = eval(input("ingrese un segundo numero"))
numero3 = eval(input("ingrese un tercer numero"))

if(numero1 <= numero2 and numero2 <= numero3):
  print("{} , {} , {}".format(numero1,numero2,numero3))
elif(numero2 <= numero1 and numero1 <= numero3):
  print("{} , {} , {}".format(numero2,numero1,numero3))
elif(numero2 <= numero3 and numero3 <= numero1):
  print("{} , {} , {}".format(numero2,numero3,numero1))
elif(numero3 <= numero2 and numero2 <= numero1):
  print("{} , {} , {}".format(numero3,numero2,numero1))
elif(numero1 <= numero3 and numero3 <= numero2):
  print("{} , {} , {}".format(numero1,numero3,numero2))
elif(numero3 <= numero1 and numero1 <= numero2):
  print("{} , {} , {}".format(numero3,numero1,numero2))