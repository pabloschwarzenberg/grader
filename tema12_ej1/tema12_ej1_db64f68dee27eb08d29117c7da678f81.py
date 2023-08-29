def combine(n,obj=""):
    if n==1:
        print(obj+"1")
        print(obj+"0")
        return
    for i in range(2):
        combine(n-1,obj+str(i))
n=int(input())
combine(n)
           