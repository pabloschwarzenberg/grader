def numero_perfecto(num):
    suma = 0
    for i in range(1, num):
        if num % i == 0:
            suma = suma + i
    if (suma == num):
        return True
    else:
        return False
 
c = 1
i = 0
 
while True:
  if numero_perfecto(c):
    print(c)
    i += 1
    if i == 4:
      break
  c += 1