def numero_perfecto(num):
    res=[i for i in range(1,num-1) if num%i==0]
    if sum(res) == num:
        return True
    else:
        return False