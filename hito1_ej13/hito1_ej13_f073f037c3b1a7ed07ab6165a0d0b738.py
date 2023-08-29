#Factores Primos
a = int(2) 
number = int(input("Ingrese número: "))

while number != 1:
    if number % a == 0:
        print(a)
        number=number/a
    else:
        a = a + 1      