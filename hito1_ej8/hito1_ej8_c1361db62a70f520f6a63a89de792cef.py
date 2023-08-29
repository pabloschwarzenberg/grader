#Descomponer un número
numero = int(input("Ingrese un numero de hasta 4 digitos: "))

if numero > 9999:
  print("El numero contiene mas de 4 digitos.")
else:
  unidades = numero % 10
  decenas = (numero // 10) % 10
  centenas = (numero // 100) % 10
  miles =(numero // 1000) % 10

print(miles,"M","+",centenas,"C","+",decenas,"D","+",unidades,"U")
