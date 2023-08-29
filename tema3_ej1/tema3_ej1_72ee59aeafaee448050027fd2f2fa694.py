if __name__ == "__main__": 
  a=int(input())


  
def divisores_a(a):
        x=[]
        for i in range(1,a):
            if a%i==0:
                x.append(i)
            else:
                i=i+1
            if i==a:
                break
        return(x)
 

def suma_divisores(a):
        r=sum(divisores_a(a))
        if r==1:
                b=True
        else:
                b=False
        return(r,b)





           