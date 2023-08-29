def nalnular_string(n,listos):
    a = '0'*n
    if n == 0:
        return listos
    else:
        if a in listos:
            return
        
        else:
            listos.append(a)
            permutar(n,listos,a)
        

        
    

def permutar(n,listos,b):
    for i in range(0,n):
        a = b
        a = a[:i]+'1'+a[i+1:]
        if a in listos:
            return
        else:
            listos.append(a)
            permutar(n,listos,a)





n = 9
listos=[]
nalnular_string(n,listos)
print(listos)