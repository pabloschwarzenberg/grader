#Ordenar tres numeros enteros de menor a mayor separados por coma
number1=int(input("Ingrese el primer n°: "))
number2=int(input("Ingrese el segundo n°: "))
number3=int(input("Ingrese el tercer n°: "))
print("EL orden de menor a mayor es: ")
primer=min(number1, number2, number3)
tercer=max(number1, number2, number3)
segundo=(number1+number2+number3)-(primer+tercer)
print(primer,",", segundo,",", tercer)