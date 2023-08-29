def amigos(a,b):
    divisores = [1]
    divisoresb = [1]

    for i in range(2, a ):
        if a % i == 0:
            divisores.append(i)
            sum(divisores)    

    for i in range(2, b ):
        if b % i == 0:
            divisoresb.append(i)
            sum(divisoresb)
    if b==(sum(divisores)) and a==(sum(divisoresb)):
        return True
    else:
        return False