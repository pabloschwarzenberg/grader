# completa el código de la función
a =3500

def suma_divisores(a):
  divisores = [i for i in range(1, a + 1) if a % i == 0]
   
  return sum(divisores)
def es_primo(a):

    contador = 0

    for i in range(1, a + 1):
        if a % 1 == 0:
            contador += 1

    if contador == 2:
        return True
    else:
        return False
print(es_primo(a))


resultado = suma_divisores(a)
print(resultado)
           