#Descomponer un número
numero = int(input("Ingrese un numero de 1 hasta 4 digitos porfavor: "))
print("descomponer numero") 
a = ((numero//1000)%10)
b = ((numero//100)%10)
c = ((numero//10)%10)
d = ((numero//1)%10)

if numero >= 1000 and numero <= 9999:
  print(a,"M+",b,"C+",c,"D+",d,"U")
elif numero >= 100 and numero <= 999:
  print(b,"C+",c,"D+",d,"U")
elif numero >= 10 and numero <= 99:
  print(c,"D+",d,"U")
elif numero >= 0 and numero <= 9:
  print(d,"U")