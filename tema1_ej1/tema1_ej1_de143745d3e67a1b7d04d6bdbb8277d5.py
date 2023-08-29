#Suma de los N primeros números
def SumaA(num) :
    s = 0
    while num > 0:
        s = s + num % 10
        num = num // 10
    return s

n = int(input("Cantidad de números: "))
SumaB = 0
while n > 0:
    num = int(input("Numeros: "))
    SumaB = SumaB + SumaA(num)
    n = n - 1

print(SumaB)          