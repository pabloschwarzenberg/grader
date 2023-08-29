#Descomponer un número

numero = int(input("Ingrese un numero natural mayor a cero y de hasta 4 dígitos: "))

if numero <= 0 or numero >= 10000:
    print("Ese número no es válido")
    numero = int(input("Ingrese un numero natural mayor a cero y de hasta 4 dígitos: "))
    
miles = numero // 1000
numero = numero - (miles*1000)

centenas = numero // 100
numero = numero - (centenas*100)

decenas = numero // 10
numero = numero - (decenas*10)

unidades = numero

if miles != 0:
  print(miles,"M + ",centenas,"C + ",decenas,"D + ",unidades,"U")

elif centenas != 0:
    print(centenas,"C + ",decenas,"D + ",unidades,"U")
    
elif decenas != 0:
    print(decenas,"D + ",unidades,"U")
    
elif unidades != 0:
    print(unidades,"U")
    
else:
    print("ERROR")
    input()