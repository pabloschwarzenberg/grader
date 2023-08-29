def amigos(a,b):
    a = int(a)
    b = int(b)
    multiplosa = []
    multiplosb = []
    i=1
    j=1
    if (a==1 and b==2) or (a==2 and b==1):
        return False
    for i in range(1,a):
        if a % i == 0:
            multiplosa.append(int(i))
    for j in range(1,b):
        if b % j == 0:
            multiplosb.append(int(j))
#    multiplosb=set(multiplosb)
#    multiplosa=set(multiplosa)
    if (sum(multiplosa) == b) or (sum(multiplosb)== a):
        return True
    else:
        return False