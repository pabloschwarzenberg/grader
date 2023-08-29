num = int(input("ingrese su numero decimal: "))
bi = str(bin(num)).replace("0b","")
num2 = int(bi)
print("resultado = ",num2)