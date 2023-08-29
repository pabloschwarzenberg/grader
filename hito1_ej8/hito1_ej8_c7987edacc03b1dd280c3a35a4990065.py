numero1=int(input("Ingrese un numero de 4 digitos: "))

numero1a=(numero1%10)
numero1b=(numero1%100)//10
numero1c=((numero1%1000)//100)
numero1d=(numero1%10000)//1000


print((str(numero1d)+("M+")) + (str (numero1c)+("C+")) + (str(numero1b)+("D+") + (str(numero1a) +("U"))))