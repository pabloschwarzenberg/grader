#Descomponer un número
# Entrada

num = int(input("Escriba un numero: "))

# Procesamiento
if len(str(num)) < 5:
    a = int(num) % 10
    b = (num//10) % 10
    c = (num//100) % 10
    d = (num//1000) % 10
    print(str(d) + "M", "+", str(c) + "C", "+", str(b) + "D", "+", str(a) + "U")
else:
    print("numero no valido")      