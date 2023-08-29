#Factores Primos
num_dos = int(2)
num_uno = int(input("Ingrese un numero: "))

while (num_uno != 1):
    if (num_uno % num_dos == 0):
      print(str(num_dos) + " ")
      num_uno = num_uno / num_dos
    else:
      num_dos = num_dos + 1 
    