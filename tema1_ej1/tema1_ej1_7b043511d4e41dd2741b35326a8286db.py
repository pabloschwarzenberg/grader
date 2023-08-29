#Suma de los N primeros números
num = int(input("Ingresa un n: "))
n = 0
f = 0
while(n != num):
        f = n + (f+1)
        n += 1
        print(f)
print(f*(f+1)/2)