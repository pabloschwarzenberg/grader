#Descomponer un número
n = input()

a=range(0,len(n))
b=""
c=["M","C","D","U"]

for i in a:
        b+=n[i]
        b+=c[(4-len(n))+i]
        if i<(len(n)-1):
                b+="+"
print(b)
        