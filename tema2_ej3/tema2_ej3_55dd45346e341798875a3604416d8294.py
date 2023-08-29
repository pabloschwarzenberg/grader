def numero_perfecto(a):
  div = list()
  sum = 0
  val = True
  for i in range(1,a):
    if a % i == 0:
      div.append(i)
  for i in div:
    sum += i
  if sum == a:
    return True
  else:  
    return False

if __name__=="__main__":
    num = int(input("Ingrese a: "))
    print(numero_perfecto(num))