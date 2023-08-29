#Factores Primos
numero = int(input("Ingrese un numero"))
i = 2
j = 1
while numero > 1:
    while j < numero:
        if numero % i == 0:
            print(i)
            break
        i += 1
    numero = numero//i
  