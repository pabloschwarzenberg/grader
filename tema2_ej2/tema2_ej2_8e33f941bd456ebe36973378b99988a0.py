def amigos(a,b):
    z=0
    for i in range(1,a + 1):
        if a % i == 0:
            if i != a:
                print(i)
                z+=i

    s=0
    for i in range(1,b + 1):
        if b % i == 0:
            if i != b:
                print(i)
                s+=i
    print(z,s)
    if s == a and z ==b:
        return True
    else: 
        return False