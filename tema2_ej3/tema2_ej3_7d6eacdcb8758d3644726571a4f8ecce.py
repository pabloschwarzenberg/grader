def numero_perfecto(a):
    s = 0
    for i in range(1,a):
      if a % i == 0:
         s += i
    if s == a:
      return (True)
    else:
      return (False)

if __name__=="__main__":   
  a = int(input("Ingrese numero: "))
  n = numero_perfecto(a)
  print(n)
 
           