x = int(input("Ingresa numero de 4 digitos: "))

if x >= 1000:
    miles = x//1000
    centenas = (x//100)%10
    decenas = (x//10)%10
    unidades = x%10
    print(miles,"M"," + ",centenas,"C"," + ",decenas,"D"," + ",unidades,"U", sep='', end='')
if 100 <= x <= 999:
    centenas = (x//100)%10
    decenas = (x//10)%10
    unidades = x%10
    print(centenas,"C"," + ",decenas,"D"," + ",unidades,"U", sep='', end='')
if 10 <= x <= 99:
    decenas = (x//10)%10
    unidades = x%10
    print(decenas,"D"," + ",unidades,"U", sep='', end='')
if x <= 9:
    unidades = x%10
    print(unidades,"U", sep='', end='')