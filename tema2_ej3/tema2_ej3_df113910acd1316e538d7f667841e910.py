def numero_perfecto(k):
    sd = 0
    for i in range(1,k):
        if (k%i==0):
            sd += i
    if sd == k:
        return True
    else:
        return False