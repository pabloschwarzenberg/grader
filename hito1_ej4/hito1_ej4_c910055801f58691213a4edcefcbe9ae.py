# Conversión de Decimal a Binario
n = float(input("Ingrese un número >>> "))
f = n
result = ""

while f != 0:
    r = n % 2
    r = r // 1
    result += str(int(r))
    int(r)
    f = n // 2
    n /= 2

result = result[::-1]
print("resultado =",(result))
      