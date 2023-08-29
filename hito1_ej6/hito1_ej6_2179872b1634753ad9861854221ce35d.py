#Ordenar tres números

n1 = eval(input())
n2 = eval(input())
n3 = eval(input())
if(n1 <= n2 <= n3):
    print("{}, {}, {}".format(n1, n2, n3))
else:
    if(n2 <= n3 <= n1):
        print("{}, {}, {}".format(n2, n3, n1))
    else:
        if(n3 <= n2 <= n1):
            print("{}, {}, {}".format(n3, n2, n1))
        else:
            if(n3 <= n1 <= n2):
                print("{}, {}, {}".format(n3, n1, n2))
            else:
                if(n1 <= n3 <= n2):
                    print("{}, {}, {}".format(n1, n3, n2))
                else:
                    if(n2 <= n1 <= n3):
                        print("{}, {}, {}".format(n2, n1, n3))