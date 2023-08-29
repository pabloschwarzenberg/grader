def mcd(a,b):
    if a>b:
        c=a
    elif b>=a:
        c=b
  
    div=1
    for i in range(1,c+1):
          if a%i==0 and b%i==0:
              div=i
    return div
    
   
def mcm(a,b,ab):
    div=mcd(a,b)
    return (ab)/div

if __name__=="__main__":
    pass

print(mcd(24,12))
print(mcm(13,29,13*29))

if __name__=="__main__":
    pass

