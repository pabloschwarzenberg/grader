#Descomponer un número
numero = int(input("Ingrese un numero:"))
num = str(numero)

if len(num) == 4:
  primer = int(num[0])
  segundo = int(num[1])
  tercer = int(num[2])
  cuarto = int(num[3])
  print(str(primer) + 'M+' + str(segundo) + 'C+' + str(tercer) + 'D+' + str(cuarto) + 'U')
elif len(num) == 3:
  primer = int(num[0])
  segundo = int(num[1])
  tercer = int(num[2])
  print(str(primer)+'C+'+str(segundo)+'D+'+str(tercer)+'U+')
elif len(num) == 2:
  primer = int(num[0])
  segundo = int(num[1])
  print(str(primer) + 'D+' +str(segundo) + 'U+')
elif len(num) == 1:
  primer = int(num[0])
  print(str(primer) + 'U+')