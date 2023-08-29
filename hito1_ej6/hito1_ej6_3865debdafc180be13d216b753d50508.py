n1 = int(input("escriba el primer numero: "))
n2 = int(input("escriba el segundo numero: "))
n3 = int(input("escriba el tercer numero: "))

a = min(n1, n2, n3)
b = max(n1, n2, n3)
c = (n1 + n2 + n3) - a - b

print("{},{},{}".format(a, c, b))


