# Conversor de Decimal a Binario

# Escribe un programa que reciba como entrada un número decimal e imprima el resultado de convertirlo a binario. Por ejemplo, al ingresar el número 33 tu programa debiera imprimir el siguiente mensaje:
# resultado=100001

num = int(input("ingrese un numero: "))
cod= bin(num)[2:]
print("resultado="+str(cod)) 