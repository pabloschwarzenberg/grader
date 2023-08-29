def mcm(a,b,ab):
    multiplo = 0
    i = 1
    while multiplo < ab:
        multiplo = a*i
        if multiplo%b==0:
            return multiplo
        i = i+1
    return ab
       

if __name__=="__main__":
    pass
           