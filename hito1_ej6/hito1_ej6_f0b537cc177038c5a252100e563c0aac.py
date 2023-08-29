a = int(input("Deposite el primer número: "))
b = int(input("Deposite el segundo número: "))
c = int(input("Deposite el tercer número: "))
if ((a <= b) and (a <= c)):
    x = a;
    if (b <= c):
        y = b;
        z = c;
    else:
        y = c;
        z = b;
elif ((b <= a) and (b < c)):
    x = b;
    if (a <= c):
        y = a;
        z = c;
    else:
        y = c;
        z = a;
else:
    x = c;
    if (a <= b):
        y = a;
        z = b;
    else:
        y = b;
        z = a;
print(x,",",y,",",z)

