def amigos(a,b):
    divisores = [1]
    divisoresb = [1]
    
    for i in range(2, a + 1):
        if a % i == 0:
            divisores.append(i)
    for i in range(2, b + 1):
        if b % i == 0:
            divisoresb.append(i)
    if a != b:
        if sum(divisores) == sum(divisoresb):
            return True
        else:
            return False
    elif a == b:
        if sum(divisores) == sum(divisoresb):
            return False
    else:
        return False
        
a = int()
b = int()
resultado =(amigos(a,b))
print(resultado)
