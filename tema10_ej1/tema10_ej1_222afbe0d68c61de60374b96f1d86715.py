def mcm(a,b,c):

    if a==b:
     return c/a

    else:
     if a>b:
        	return mcm(a-b,b,c)
     else:
        	return mcm(a,b-a,c)

if __name__=="__main__":
    pass
           