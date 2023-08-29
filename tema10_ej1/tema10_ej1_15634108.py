def mcm(a,b,ab):
    if a == b:
        return ab/a
    elif a>b:
        return ab/mcm(a-b,b,ab)
    else:
        return ab/mcm(a,b-a,ab)

if __name__=="__main__":
    pass
           