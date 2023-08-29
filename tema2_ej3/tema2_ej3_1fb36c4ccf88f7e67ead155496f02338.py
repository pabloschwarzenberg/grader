def numero_perfecto(a):
    suma_a = 0     #Suma de los divisores de a
    for i in range(1,a):
        if a % i == 0 and i != a:
            suma_a += i
    if suma_a == a:
        return True
    else:
        return False
if __name__=="__main__":       
  n = int(input("Ingrese n: "))
  suma_n = 0
  i = 0 
  count = 0
  while count < n:
    if numero_perfecto(i):
      suma_n += i
      count += 1
      i += 1
    else:
      i += 1
  print(suma_n)	
           