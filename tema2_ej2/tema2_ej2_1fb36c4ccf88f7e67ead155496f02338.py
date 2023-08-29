# completa el código de la función

def amigos(a,b):
    suma_a = 0
    suma_b = 0
    for k in range(1,a):
      if a % k == 0 and k != a:
        suma_a += k
    for i in range(1,b):
        if b % i == 0 and i != b:
           suma_b += i
    if suma_a == b and suma_b == a:
        return True
    else:
        return False

           