#ordene los numeros
numero1=int(input("ingrese un numero entero: "))
numero2=int(input("ingrese un numero entero distinto al anterior: "))
numero3=int(input("ingrese un numero entero distinto a los anteriores: "))

if (numero1>=numero2>=numero3):
  print("sus numeros ordenados de menor a mayor son",numero3,",",numero2,",",numero1)

elif (numero1>=numero3>=numero2):
  print("sus numeros ordenados de menor a mayor son",numero2,",",numero3,",",numero1)

elif (numero2>=numero1>=numero3):
  print("sus numeros de menor a mayor son",numero3,",",numero1,",",numero2)

elif (numero2>=numero3>=numero1):
  print("sus numeros ordenados de menor a mayor son",numero1,",",numero3,",",numero2)

elif (numero3>=numero1>=numero2):
  print("sus numeros ordenados de menor a mayor son",numero2,",",numero1,",",numero3)

elif (numero3>=numero2>=numero1):
  print("sus numeros ordenados de menor a mayor son",numero1,",",numero2,",",numero3)