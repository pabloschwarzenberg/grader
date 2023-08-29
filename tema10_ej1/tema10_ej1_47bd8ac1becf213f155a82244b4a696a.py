def mcm(a,b,ab):
    if a==b:
        return ab/a
    elif a>b:
        return ab/mcm(a-b,b,ab)
    elif a<b:
        return ab/mcm(a,b-a,ab)