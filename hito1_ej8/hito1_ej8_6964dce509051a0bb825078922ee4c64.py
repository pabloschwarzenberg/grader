#Descomponer un número
num = int(input('Ingresa un número de hasta 4 cifras: '))  
res = num

d1= num%10
num= num//10

d2= num%10
num= num//10

d3= num%10
num= num//10

d4= num%10

if 0 <= res <= 9:
  cadenaDeCaracteres = str(d1) + 'U'
  print(cadenaDeCaracteres)
  
if 10 <= res <= 99:
  cadenaDeCaracteres = str(d2) + 'D +' + str(d1) + 'U' 
  print(cadenaDeCaracteres)

if 100 <= res <= 999:
  cadenaDeCaracteres = str(d3) + 'C +' + str(d2) + 'D +' +str(d1) + 'U'
  print(cadenaDeCaracteres)

if 1000 <= res <= 9999:
  cadenaDeCaracteres = str(d4) + 'M +' + str(d3) + 'C +' + str(d2) + 'D +' +str(d1) + 'U'
  print(cadenaDeCaracteres)