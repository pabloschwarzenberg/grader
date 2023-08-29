#Descomponer un número
def descomponer(num):
    print("Descomponer el numero: ", num)
    print(num // 1000,"M","+",num % 1000 // 100,"C","+",num % 100 // 10,"D","+",num % 10,"U")
print("Ingresa un numero de hasta 4 digitos: ")
num = int(input())
descomponer(num)    