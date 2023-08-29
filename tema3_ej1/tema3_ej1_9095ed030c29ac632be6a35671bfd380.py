
 def suma_divisores(numero):
     suma = 0
     for i in range(1, numero):
         if numero % i == 0:
             suma += i
     return suma

if __name__ == "__main__":
numero = int(input("Ingresa el número: "))
print("La suma es de sus divisores es: ")
print(suma_divisores(numero))           