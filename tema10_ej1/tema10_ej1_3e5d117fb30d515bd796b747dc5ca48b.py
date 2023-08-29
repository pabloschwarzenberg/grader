def mcm(a,b,ab):
    if b == 0:
        return int(ab/a)
    else:
        return mcm(b,a%b,ab)
print(mcm(88,44,88*44))

if __name__=="__main__":
    pass
           