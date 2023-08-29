a = str(input(" "))

if len(a) == 1:
    print(a[0], "U")
if len(a) == 2:
    print(a[0], "D +", a[1], "U")
if len(a) == 3:
    print(a[0], "C +", a[1], "D +", a[2], "U")
if len(a) == 4:
    print(a[0], "M +", a[1], "C +", a[2], "D +", a[3], "U")
else:
    print("No posible en este sistema")
