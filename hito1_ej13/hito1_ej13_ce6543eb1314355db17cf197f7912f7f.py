x = int(input('Ingrese el dato: '))
n = 2
while n<=x:
    while x%n == 0: #Probar el divisor n
         print("Divisor: ", n)
         x=x/n #Reducir el dato x
    n=n+1