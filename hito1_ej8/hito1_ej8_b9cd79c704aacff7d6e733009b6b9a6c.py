#Descomponer un número
print("Introduce el número: ")
numero = int(input ())

umill = int(numero / 1000)
residuo = numero % 1000
centenas = int(residuo / 100)
residuo = residuo % 100
decenas = int(residuo / 10)
unidades = int(residuo % 10)

umill_str = str(umill)
centenas_str= str(centenas)
decenas_str=str(decenas)
unidades_str=str(unidades)

umill_str += 'M+' 
centenas_str += 'C+'
decenas_str += 'D+'
unidades_str += 'U'


numero_str = str(numero)
if len(numero_str) == 4:
  print(umill_str, centenas_str, decenas_str, unidades_str)
elif len(numero_str) == 3:
  print(centenas_str, decenas_str, unidades_str)
elif len(numero_str) == 2:
  print(decenas_str, unidades_str)
elif len(numero_str) == 1:
  print(unidades_str)
