##12.-conversor de decimal a binario
def bindec(n):
    s=0
    i=0
    print("el binario",n,end="")
    while(n>=1):
        d=n%10;
        n=int(n/10);
        s=s+d*pow(2,i);
        i=i+1

    print("corresponde al numero",s)

def decbin(n):
    d=[]
    print("el numero",n,end="")
    while(n>=1):
        d.append(n%2);
        n=int(n/2);

    S=d[::-1]
    
    print("corresponde al binario",end="")
    [print(k,end="")for k in S]

decbin=int(input(""))