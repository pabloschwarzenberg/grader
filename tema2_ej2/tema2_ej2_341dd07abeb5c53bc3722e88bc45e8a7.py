# completa el código de la función
def div(n):
    vec=[]
    for i in range(1,n):
        if n%i==0:
            vec.append(i)
    return vec
def sum(vec):
    sum=0
    for k in vec:
        sum=sum+k
    return sum



           