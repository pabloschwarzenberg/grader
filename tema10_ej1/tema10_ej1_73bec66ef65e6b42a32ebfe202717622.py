def mcm(a,b,ab):
    if a > b:
        division = int(a//b)
        resto = int(a%b)
        if a == b:
            return float(a)
        if resto == 0:
            return (ab)/b
        else:
            a = b
            b = resto
            return mcm(a,b,ab)
    if b > a:
        division = int(b//a)
        resto = int(b%a)
        if a == b:
            return float(b)
        if resto == 0:
            return (ab)/a
        else:
            b = a
            a = resto
            return mcm(b,a,ab)