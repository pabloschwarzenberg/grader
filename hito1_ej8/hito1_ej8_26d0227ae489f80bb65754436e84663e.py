#Descomponer un número
numero=int(input("Ingrese un numero de 4 unidades: "))
digito1=int(numero/1000)
x=int(numero/100)
digito2=x % 10
y=numero % 100
digito3=int(y/10)
digito4=y % 10

print(digito1,"M +", digito2,"C +", digito3,"D +", digito4,"U")