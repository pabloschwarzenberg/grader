def numero_perfecto(a):
    n = 1
    sum = 0
    while n<a:
        if a%n == 0:
            sum = sum+n
        n = n+1
    if(a == sum):
        return True
    else:
        return False
           