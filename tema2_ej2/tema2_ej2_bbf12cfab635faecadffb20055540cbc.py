def amigos(a,b):
    friend1 = 0
    friend2 = 0
    for i in range(1,a):
        if a%i==0:
            friend1+=i
    if friend1 !=b:
        return False
    for f in range(1,b):
        if b%f==0:
            friend2 +=f
    if friend2 !=a:
        return False
    return True