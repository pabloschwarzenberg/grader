def numero_perfecto(a):
 divisoresA=[]
 sumaA = 0
 for i in range(1, a+1):
  if a % i == 0:
   divisoresA.append(i)
 for i in divisoresA:
  if i == a:
   divisoresA.remove(i)
 for i in divisoresA:
  sumaA += i
 if sumaA == a:
  return True
 else:
  return False


if __name__ =="main":
 a=int(input("Ingrese a: "))
 print(numero_perfecto(a))