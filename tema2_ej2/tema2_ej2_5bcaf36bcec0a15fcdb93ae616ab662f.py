a=0
b=0
def suma(N, S):
    if a!=b:
        for i in range(2, N):
            if (N % i == 0):
                S = S + i             
        return S
    else:
        print("no se puede repetir")
sum1, sum2 = 1, 1
if __name__ == "__main__":
  a = int(input("ingrese primer numero"))
if __name__ == "__main__":
  b = int(input("ingrese segundo numero"))
sum1 = suma(a, sum1)
sum2 = suma(b, sum2)
if ((sum1 == b) and (sum2 == a)):
   True
else:
   False