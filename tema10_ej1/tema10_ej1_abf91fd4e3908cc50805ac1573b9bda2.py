def mcm(a,b,ab):
    if a%b == 0:
        div = a/b
        return (b*div)
    return mcm(a+(ab/b),b,ab)

if __name__=="__main__":
    pass
           