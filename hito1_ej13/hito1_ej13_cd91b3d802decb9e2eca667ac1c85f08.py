def esPrimo(x):
  if(x<1):
    return False
  elif(x==2):
    return True
  else:
    for i in range(2,x):
      if(x%i==0):
        return False
    return True

print("***FACTORES PRIMOS***")
num=int(input("Ingrese el número: "))

if(num==1):
    print(1)
else:
  for i in range(0,num+1):
    if(esPrimo(i)==True and num%i==0):
      if(i==1):
        None
      else:
        print(i)
