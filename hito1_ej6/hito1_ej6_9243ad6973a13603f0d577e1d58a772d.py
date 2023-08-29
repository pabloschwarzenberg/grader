num1 = eval(input("Inserte el numero 1: " ))
num2 = eval(input("Inserte el numero 2: " ))
num3 = eval(input("Inserte el numero 3: " ))
if num1 < num2 and num1 < num3:
    a = num1
    if num2 < num3:
        b = num2
        c = num3
    else:
        b = num3
        c = num2
else:
    if num2 < num1 and num2 < num3:
        a = num2
        if num1 < num3:
            b = num1
            c = num3
        else:
            b = num3
            c = num1
    else:
        if num3 < num2 and num3 < num1:
            a = num3
            if num2 < num1:
                b = num2
                c = num1
            else:
                b = num1
                c = num2
print("{},{},{}".format(a,b,c))