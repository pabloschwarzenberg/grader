#Descomponer un número
n = int(input("Ingrese numeros de 4 digitos : "))
unidades = n % 10
n//=10
decenas = n % 10
n//=10
centenas = n % 10
n//=10
milesimas = n % 10
n//=10

print(milesimas,"M + ", centenas,"C + ", decenas,"D + ",unidades,"U ")
      