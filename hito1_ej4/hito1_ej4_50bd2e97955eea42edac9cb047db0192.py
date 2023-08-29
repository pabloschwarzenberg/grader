def dab(n):
    if n <= 0:
        return "0"
    b= ""
    while n > 0:
        residuo = int(n % 2)
        n = int(n/ 2)
        b = str(residuo) + b
    return b


n = int(input("decimal para binario : "))
b = dab(n)
print("resultado=", b)


