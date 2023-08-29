# completa el código de la función
def amigos(a,b):
    ldiv_a = ldiv_a=[i for i in range(1,a) if a % i == 0]
    ldiv_b =  ldiv_b=[i for i in range(1,b) if b % i == 0]

    suma_a = 0
    suma_b = 0

    for j in ldiv_a:
        suma_a = suma_a+j
    for j in ldiv_b:
        suma_b = suma_b+j
    if suma_a == b and suma_b == a:
        return True
    else:
        return False
if __name__ == "__main__":
  a = input("ingrese numero 1:")
  b = input("ingrese numero 2:")

  a = int(a)
  b = int(b)
  print(amigos(a,b))
           