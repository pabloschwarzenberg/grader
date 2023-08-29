def mcm(a,b,ab):
    if a%b==0:
        return ab/b
    else:
        return mcm(b,a%b,ab)
        
if __name__=="__main__":
    pass
           