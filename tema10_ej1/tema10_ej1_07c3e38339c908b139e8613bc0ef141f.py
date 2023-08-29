def mcm(a,b,ab):
    resto = a%b
    if resto == 0:
        return ab / b

    if resto != 0:
        return mcm(b,resto,a*b)