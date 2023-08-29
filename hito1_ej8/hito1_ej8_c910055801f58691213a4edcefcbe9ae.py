#Descomponer un número
num = int(input(">>> "))

if num < 10000:
    U = str(num % 10)+"U"

    D = str((num % 100)//10)+"D"

    C = str((num % 1000)//100)+"C"

    M = str(num//1000)+"M"


print(M,"+",C,"+",D,"+",U)