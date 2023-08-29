def sum_div(a):
  suma = 0
  e = 1
  while e<a:
     if a%e==0:
       suma = suma + e
     e=e+1
  return suma

def numero_perfecto(a):
    if sum_div(a)==a:
        return True
    else:
        return False

if __name__=="__main__":
    a=int(input("Ingrese a: "))
    print(numero_perfecto(a))
    n = int(input())
    suma = 0
    for i in range(1,n):
        if numero_perfecto(i):
            suma = suma + i
    print(suma)
           