def amigos(a, b):
    sa=0
    sb=0
    for i in range(1,a):
        if a%i==0:
            sa+=i

    for e in range(1,b):
        if b%e==0:
            sb+=e

    return sa==b and sb== a