# por favor escribe aquí tu función
numero = 0
while numero <= 1:
 numero = int(input("Ingresa un número: "))
## Proceso:
divisor = 2
cont = 0
mitad = numero/2
while divisor <= mitad:
if numero%divisor == 0:
 cont = cont+1
 divisor = divisor+1
## Salida de datos:
if cont == 0:
 print(f"\nEl número {numero} es primo.\n")
else:
 print(f"\nEl número {numero} es compuesto.\n")
  
      
       