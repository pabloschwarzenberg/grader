def mcd(a,b):
    if a == b:
       return b
    elif a > b :
       return mcd(b,a-b)
    else :
       return mcd(a,b-a)
      
def mcm (a,b,ab):
    d=mcd(a,b)
    mcm=a*b/d
    print(mcm)
    return mcm


if __name__=="__main__":
   a = int(input("Introduce el primer numero: "))
   b = int(input("Introduce el segundo numero: "))
   ab= a*b
   c=mcm(a,b,ab)
           