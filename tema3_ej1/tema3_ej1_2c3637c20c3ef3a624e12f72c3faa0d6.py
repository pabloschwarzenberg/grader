#Soy Oscar Páez
def suma_divisores(num):
    suma = 0
    for i in range(1, num):
        if num % i == 0:
            suma += i
    
    if suma == 1:
        a = True
    else:
        a = False
    return suma, a   
    
   
if __name__ == "__main__":
    num = int(input("Ingrese un numero: "))
    print(suma_divisores(num))
   
  
    