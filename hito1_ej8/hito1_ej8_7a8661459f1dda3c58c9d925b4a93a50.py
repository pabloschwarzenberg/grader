#Descomponer un número

num_ing = int(input("Ingrese un numero de 4 digitos : "))
largo = len(str(num_ing))
if largo == 4:
    miles = num_ing / 1000
    num_ing = num_ing % 1000
    centenas = num_ing / 100
    num_ing = num_ing % 100
    decenas = num_ing / 10
    unidades = num_ing % 10
    print("RESULTADO ES: %dM + %dC + %dD + %dU" %(miles,centenas,decenas,unidades))
if largo == 3:
    centenas = num_ing / 100
    num_ing = num_ing % 100
    decenas = num_ing / 10
    unidades = num_ing % 10
    print("RESULTADO ES: %dC + %dD + %dU" %(centenas,decenas,unidades))
if largo == 2:
    decenas = num_ing / 10
    unidades = num_ing % 10
    print("RESULTADO ES: %dD + %dU" %(decenas,unidades))
if largo == 1:
    print("RESULTADO ES: %dU" %(num_ing))