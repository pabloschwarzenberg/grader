#Ordenar tres números
numero1 = int(input("escriba un numero entero: "))
numero2 = int(input("escriba un numero entero: "))
numero3 = int(input("escriba un numero entero: "))

a = min(numero1, numero2, numero3)
b = max(numero1, numero2, numero3)
c = (numero1 + numero2 + numero3)- a - b 

print(a,',',c,',',b)