#Descomponer un número
num = int(input("Ingrese un número de hasta cuatro dígitos: "))

if 0<num<10000:

  mil = num//1000

  centena = (num%1000)//100

  decena = ((num%1000)%100)//10

  unidad = ((num%1000)%100)%10

  print(mil,"M+",centena,"C+",decena,"D+",unidad,"U")
elif 0<num<100:
  print(decena,"D+",unidad,"U")
