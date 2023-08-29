#Factores Primos
i = 1
x = int(input("Ingrese un numero: "))
for k in range(1, (x + 1), 1):
    c = 0
    for j in range(1, (i + 1), 1):
        a = i % j
        if (a == 0):
            c = c + 1

    if (c == 2):

        print(i)
    else:
        k = k - 1

    i = i + 1
print("Estos son los numeros primos hasta", x, )
print("----------------------------------------------------")
t = x
p = 1
c = 3
r = '2'
while p < t:
    fact1 = math.factorial(c - 1)
    if fact1 % c == c - 1:
        r = r + ',' + str(c)
        p += 1
    c += 1
print("los primeros", x, "numeros primos son: ", r, )