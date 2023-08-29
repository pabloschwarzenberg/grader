string=input("Ingresar string: ")
n=int(input("Ingresar entero n: "))
mydict={}

for i in range(len(string)-n+1):
    sub_string=string[i:i+n]
    if sub_string not in mydict.keys():
        mydict[sub_string]=1
    else:
        mydict[sub_string]=mydict[sub_string]+1
flag=0
for key,value in mydict.items():
    if value==1:
        flag=1
        print(key)
if flag==0:
    print(None, "ninguna")