# por favor escribe aquí tu función
num = int(2)
primo = float(input("Ingrese el numero: "))
while(primo != 1):
    if (primo % num == 0 ):
        print(str(num) + "")
        primo = primo / num
    else:
        num = num + 1
