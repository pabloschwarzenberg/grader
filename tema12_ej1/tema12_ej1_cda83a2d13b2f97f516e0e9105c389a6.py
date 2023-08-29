n = int(input())
def combinaciones(n, s ='') :
    if n > 1 :
        for i in range(2) :
            combinaciones(n-1, s + str(i))
        return
    for i in range(2) :
        print(s + str(i))
combinaciones(n)