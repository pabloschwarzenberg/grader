# completa el código de la función
def suma_divisores(a):
     divisores = []
     for i in range(1, a):
         if (a % i) == 0:
             divisores.append(i)
     if sum(divisores) == 1:
         return 1, True
     else:
         return sum(divisores), False


if __name__ == '__main__':
     valor = int(input("ingrese el valor: "))
     print(suma_divisores(valor))
