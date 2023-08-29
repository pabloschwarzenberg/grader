# completa el código de la función
def amigos(a,b):
    sum_a = 0
    sum_b = 0
    
    if a == 1 or b == 1:
        return False
    
    for i in range(1, a + 1):
        print(i)
        print(a%i)
        if a%i == 0 and a != i:
            sum_a += i

    for j in range(1, b + 1):
        if b%j == 0 and b != j:
            sum_b += j

    if (sum_a == b or sum_b == a) and a != b:
        return True
        
    else:
        return False
        
