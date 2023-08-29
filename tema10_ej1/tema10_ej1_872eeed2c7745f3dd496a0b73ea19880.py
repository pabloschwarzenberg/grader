def mcd(a,b,s):

    if a%b==0:

        s.append(b)

        s=s.copy()

        return b

    elif a==b:

        return 1

    resto=a%b

    mcd(b,resto,s)

    return s[0]

def mcm(a,b,c):

    m=mcd(a,b,[])

    return c/m

if __name__=="__main__":
    pass
           