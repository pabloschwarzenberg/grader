# completa el código de la función
def suma_divisores(a):
    s = 0
    for i in range(1,a):
      if a % i == 0:
         s += i
    if s == 1:
      return (1, True)
    else:
      return (s, False)

if __name__=="__main__":   
  a = int(input("Ingrese numero: "))
  n = suma_divisores(a)
  print(n)
  
  