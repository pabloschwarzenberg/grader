b = eval(input("Ingrese el Número: "))
a = eval(input("Ingrese la hora: "))

cond1 = (a >= 0 and a <= 7)
cond2 = (a < 14 and a > 7)
cond3 = ((b%1000)==909)
cond4 = (a >= 17 and a <= 19)
cond5 = ((b//100000)==877)
cond6 = (a > 19)
cond7 = (a < 17 and a >= 14)
if cond1 == True:
    print("CONTESTAR")
else:
    if cond2 == True:
        if cond3 == True:
            print("CONTESTAR")
        else:
            print("NO CONTESTAR")
    else:
        if cond7 == True:
            print("NO CONTESTAR")
        else:
            if cond4 == True:
                if cond5 == True:
                    print("NO CONTESTAR")
                else:
                    print("CONTESTAR")
            else:
                if cond6 == True:
                    print("NO CONTESTAR")
                else:
                    print("NO CONTESTAR")
