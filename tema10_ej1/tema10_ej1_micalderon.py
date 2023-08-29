def mcm(a,b,ab):
    if b==0:
        return ab/a
    else:
        return mcm(b,a%b,ab)

if __name__=="__main__":
    print(mcm(88,44,88*44))
           