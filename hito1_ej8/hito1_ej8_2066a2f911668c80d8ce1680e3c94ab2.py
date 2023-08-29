#Descomponer un número
n = int(input("ingrese numero: "))

if n<= 9999:
    unidades = n % 10
    decenas = (n // 10) % 10
    centenas = (n // 100) % 10
    miles = n // 1000
    print(miles, "M +", centenas, "C +", decenas, "D +", unidades, "U")

      