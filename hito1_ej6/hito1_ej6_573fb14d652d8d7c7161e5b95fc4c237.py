x = int(input("primer numero:"))
y = int(input("segundo numero:"))
z = int(input("tercer numero:"))
Min = min(x, y, z)
Max = max(x, y, z)
Med = x + y + z - Min - Max
print("{}, {}, {}".format(Min, Med, Max))