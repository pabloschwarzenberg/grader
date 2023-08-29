def suma_divisores(a):
    suma = 0
    primo = 0
    for i in range(1,a+1):
        if a % i == 0:
            print(i)
            suma += i
            if suma-a == 1:
              primo = True
            else:
              primo = False

    return (suma-a,primo)
if __name__ == "__main__":
  a = int(input("Ingrese un numero:"))       
  print("La suma de sus divisores es:",suma_divisores(a))






