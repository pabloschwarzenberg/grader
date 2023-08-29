#Descomponer un número
number = int(input("Ingrese un numero: "))
largo = len(str(number))
if largo == 1:
    print(number,"U")
if largo == 2: 
    decena = (number // 10)
    unidad = (number % 10)
    print(decena,"D", "+", unidad,"U")
if largo == 3: 
    centena = (number // 100)
    decena = (number // 10) % 10
    unidad = (number % 10)
    print(centena,"C", "+", decena,"D", "+", unidad,"U")
if largo == 4:
    milesima = number // 1000
    centena = (number // 100) %10
    decena = (number // 10) % 10
    unidad = (number % 10)
    print(milesima, "M", "+", centena,"C", "+", decena,"D", "+", unidad,"U")