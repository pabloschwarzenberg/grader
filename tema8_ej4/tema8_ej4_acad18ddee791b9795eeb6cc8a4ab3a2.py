def rot13(a):
    b=list(a)
    
    for i in range(len(b)):
            if b[i] =="a":
                b[i]="n"
            elif b[i] =="n":
                b[i]="a"
            else:
                continue
    for i in range(len(b)):
            if b[i] =="b":
                b[i]="o"
            elif b[i] =="o":
                b[i]="b"

            else:
                continue
    for i in range(len(b)):
            if b[i] =="c":
                b[i]="p"
            elif b[i] =="p":
                b[i]="c"
            else:
                continue
    for i in range(len(b)):
            if b[i] =="d":
                b[i]="q"
            elif b[i] =="q":
                b[i]="d"
            else:
                continue
    for i in range(len(b)):
            if b[i] =="e":
                b[i]="r"
            elif b[i] =="r":
                b[i]="e"
            else:
                continue
    for i in range(len(b)):
            if b[i] =="f":
                b[i]="s"
            elif b[i] =="s":
                b[i]="f"
            else:
                continue
    for i in range(len(b)):
            if b[i] =="g":
                b[i]="t"
            elif b[i] =="t":
                b[i]="g"
            else:
                continue
    for i in range(len(b)):
            if b[i] =="h":
                b[i]="u"
            elif b[i] =="u":
                b[i]="h"
            else:
                continue
    for i in range(len(b)):
            if b[i] =="i":
                b[i]="v"
            elif b[i] =="v":
                b[i]="i"
            else:
                continue
    for i in range(len(b)):
            if b[i] =="j":
                b[i]="w"
            elif b[i] =="w":
                b[i]="j"
            else:
                continue
    for i in range(len(b)):
            if b[i] =="k":
                b[i]="x"
            elif b[i] =="x":
                b[i]="k"
            else:
                continue
    for i in range(len(b)):
            if b[i] =="l":
                b[i]="y"
            elif b[i] =="y":
                b[i]="l"
            else:
                continue
    for i in range(len(b)):
            if b[i] =="m":
                b[i]="z"
            elif b[i] =="z":
                b[i]="m"
            else:
                continue



    
    c="".join(b)
    return c
    