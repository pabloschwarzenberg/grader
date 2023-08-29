def numero_perfecto(a):
    Sum = 0
    for i in range(1, a):
        if(a % i == 0):
            Sum = Sum + i
    if (Sum == a):
        return True
    else:
        return False
           