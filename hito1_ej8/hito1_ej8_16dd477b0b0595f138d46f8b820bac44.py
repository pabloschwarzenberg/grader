x = input("x= ")
xl = len(x)
if xl == 4:
    print(x[0],"M","+",x[1],"C","+", x[2],"D","+", x[3],"U")
if xl == 3:
    print(x[0],"C","+", x[1],"D","+", x[2],"U")
if xl == 2:
    print(x[0],"D","+",x[1],"U")
if xl == 1:
    print(x[0],"U")
