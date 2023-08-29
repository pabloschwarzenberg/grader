# completa el código de la función
def amigos(a,b):
    count1 = 0
    count2 = 0
    for i in range (1, a):
        if(a % i == 0):
            count1 = count1 + i
    for j in range (1, b):
        if(b % j == 0):
            count2 = count2 + j
    print(count1,count2, a,b)
    if count1 == b and count2 == a:
        return True
    else:
        return False
           