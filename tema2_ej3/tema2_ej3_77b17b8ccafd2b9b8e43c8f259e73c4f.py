# completa el código de la función
def suma_divisores(a):
  suma = 0
  primo = False
  for i in range(1,a):
    if(a%i == 0):
      suma = suma +i
  if suma == 1:
    primo = True
  return (suma, primo)


def numero_perfecto(a):
    suma = suma_divisores(a)[0]
    resultado = False
    if(suma == a):
      resultado = True
    return resultado

if __name__=="__main__":
    a=int(input("Ingrese a: "))
    print(numero_perfecto(a))
           