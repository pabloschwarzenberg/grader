#asumiendo a>b
def mcm(a,b,c):
    if a%b==0:
        return c/b
    else:
        x=a%b
        return mcm(b,x,c)
 
if __name__=="__main__":
    pass
           