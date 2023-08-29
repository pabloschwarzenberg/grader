#Conversión de Decimal a Binario
print("conversor decimal a binario")

n = int(input("Ingresa un número: "))
# 33
# 33//2 = 16  y Resto = 1
#16//2 = 8  y resto = 0
#8//2 = 4 y resto = 0
#4 //2 = 2 y resto = 0
#2 //2 = 1 y resto 0
#1 //2 = 0 y resto 1
acum = ""

while n > 0:
    resto = n%2
    n = n//2
    acum = str(resto) + acum # 1,10, 100, 1000,10000, 100001
    #print("n= ", n, " resto= ", resto)
    #print("Su forma binaria es: ", acum)
print("resultado="+str(acum))
         