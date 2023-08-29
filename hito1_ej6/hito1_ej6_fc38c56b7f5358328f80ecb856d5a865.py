a=int(input("ingresa el primero numero: "))
b=int(input("ingresa el segundo numero: "))
c=int(input("ingresa el tercer numero: "))

if a <= b and b <= c:
    print(str(a)+ "," +str(b)+ "," + str(c))
if a >= b and b >= c:
    print(str(c)+ "," +str(b)+ "," + str(a))
if a <= b and b >= c:
    print(str(a)+ "," +str(c)+ "," + str(b))
if a >= b and b <=c:
    print(str(b) + "," + str(a) + "," + str(c))