def numero_perfecto(a):
    sumatoria=0
    for i in range(1, a):
        if a % i==0:
            sumatoria +=i
    if sumatoria == a:
        return True
    else:
        return False