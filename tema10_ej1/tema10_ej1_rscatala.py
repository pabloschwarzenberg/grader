def mcm(a,b,a*b):
    if a == b:
       return a
    elif a > b:
       return (a/(a-b))*mcm(a-b,b,(a-b)*b)
    elif a < b:
       return (b/(b-a))*mcm(a,b-a,a*(b-a))

if __name__=="__main__":
    print(mcm(88,44,88*44))
           