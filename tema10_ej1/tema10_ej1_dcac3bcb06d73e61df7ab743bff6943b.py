def mcm(a, b, ab):
    if a >= b:
        c = a % b
        if a % b == 0:
            return (ab) / b
        else:
            bc = b * c
            return mcm(b, c, ab)
    elif b > a:
        c = b % a
        if b % a == 0:
            return (ab) / a
        else:
            ac = a * c
            return mcm(a, c, ab)
    

if __name__=="__main__":
    pass
           