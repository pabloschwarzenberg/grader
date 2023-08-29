#La suma de los primeros n numeros naturales

num = int(input("ingrese un número: "))

#ocupo "round para sacarle el decimal"
suma = round(num * (num + 1) /2)

print ("suma de los " + str(num) + " primeros números naturales es: 2" + str(suma))
