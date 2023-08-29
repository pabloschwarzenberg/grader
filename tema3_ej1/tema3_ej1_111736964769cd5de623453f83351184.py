# completa el código de la función
def suma_divisores(a):
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
 a = sumaA
 if sumaA == 1:
  return a, True
 else:
  return a, False
if __name__ == "__main__":
 a=int(input(""))
 x=suma_divisores(a)
 print (x)