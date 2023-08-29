def mcm(a,b,ab):
  def mcm(a,b,ab):      
    if b%a==0:
        return a
        
    else:
        r= b%a
        ar=a*r
        print('c=',r,'a= ',a)
        mcd=mcm(r,a,ar)
        print(ab,mcd)
        return ab/mcd

if __name__=="__main__":
    pass
           