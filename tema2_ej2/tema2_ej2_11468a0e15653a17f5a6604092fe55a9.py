# completa el código de la función
def suma(N, S):
    for i in range(2, N):
        if (N % i == 0):
            S = S + i
    return S


sum1, sum2 = 1, 1
a = int(input("ingrese primer numero\n"))
b = int(input("ingrese segundo numero\n"))
sum1 = suma(a, sum1)
sum2 = suma(b, sum2)
if ((sum1 == b) and (sum2 == a)):
    print("los numeros " + str(a) + " y " +
          str(b) + " True")
else:
    print("los numeros " + str(a) + " y " +
          str(b) + " False")
           