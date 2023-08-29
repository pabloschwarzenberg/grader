#Suma de los N primeros números
def Suma(a):
    Sum = a * (a + 1) / 2
    return Sum

n = int(input("Ingrese N:"))
print(Suma(n))