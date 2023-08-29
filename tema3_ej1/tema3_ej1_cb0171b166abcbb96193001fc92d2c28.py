# completa el código de la función
def suma_divisores(n):
     if n == 1 :
        return 0 , False
     divisores = [i for i in range(1, n + 1 ) if n % i == 0 ]
     suma = sum (divisores)- n
     if suma == 1:
               return (suma,True) 
     else:
               return (suma,False)
if __name__ == "__main__":
    a = int(input("Ingrese un numero: "))
    print(suma_divisores(a))            
     


