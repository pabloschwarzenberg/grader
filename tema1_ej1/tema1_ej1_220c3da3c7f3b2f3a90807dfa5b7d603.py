#suma de los N primeros números
n = int(input("cantidad de numeros: "))
num = int(input("numero: "))
sumat = 0
while n > 0:
    sumat = sumat + sumadigitos (num)
    n = n - 1
    print(sumat)

print(sumat)

def sumadigitos (num) :
    s = 0 #suma de los digitos este numero
    while num > 0:
        s = s + num % 10
        num = num // 10
     