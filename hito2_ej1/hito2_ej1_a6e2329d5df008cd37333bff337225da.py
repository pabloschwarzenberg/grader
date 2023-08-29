def alineamiento(sec1, sec2):
    secf= ""
    sec2 = list(sec2)
    for amino in sec1:
        if len(sec2) == 0:
            break
        elif amino == sec2[0]:
            secf += sec2[0]
            sec2.pop(0)
        else:
            secf += "_"
    if len(sec2) > 0:
        for left in sec2:
            secf += left
    print([secf])
    
a = input()
b = input()
alineamiento(a, b)