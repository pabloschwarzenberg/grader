a = int(input("Ingrese número:"))

binario = ""

while a != 0 :
    resto = a % 2
    a = a// 2
    binario+= str(resto)

print("resultado=",binario[::-1])