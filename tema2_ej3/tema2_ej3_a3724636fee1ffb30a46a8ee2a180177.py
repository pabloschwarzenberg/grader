def numero_perfecto(n):
  suma = 0
  for i in range (1,n):
    if(n % i == 0):
      suma += i
  if n == suma:
    return True 
  else:
    return False 

if __name__=="__main__":
  n = int(input("introduzca el numero: "))
  if numero_perfecto(n):
    print("%s es un numero perfecto" % n)
  else:
    print("%s NO es un numero perfecto" % n)
  
           