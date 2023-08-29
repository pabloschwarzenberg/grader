def numero_amigos(a,b):
    atotal = 1
    i = 2
    while (i<a):
        r = a%i
        if (r==0):
            atotal = atotal+i
        i = i+1
    btotal = 1
    j = 2
    while (j<b):
        r = b%j
        if (r==0):
            btotal = btotal+j
        j = j+1
    if (atotal==b and btotal==a):
        print(True)
    else:
        print(False)