num = int(input("Número: "))
m = str(num // 1000)
num %= 1000
c = str(num // 100)
num %= 100
d = str(num // 10)
num %= 10
u = str(num // 1)

print(m + "M + " + c + "C + " + d + "D + " + u + "U")