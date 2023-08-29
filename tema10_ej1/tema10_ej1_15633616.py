def euclides(a,b):
    if a==b:
        return a
    if a>b:
        return euclides(a-b,b)
    if b>a:
        return euclides(a,b-a)

def mcm(a,b,ab):
    return ab/euclides(a,b)
    pass

if __name__=="__main__":
    pass
           