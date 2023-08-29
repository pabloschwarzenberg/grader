val1 = int(input("ingrece el primer valor:"))
val2 = int(input("ingrece el segundo valor:"))
val3 = int(input("ingrece el tercer valor:"))
x = min(val1, val2, val3)
y = max( val1, val2, val3 )
z = (val1 + val2 +val3)- x - y
print("los valores ordenados de de menor a mayor es:", x,',', z,',',y)