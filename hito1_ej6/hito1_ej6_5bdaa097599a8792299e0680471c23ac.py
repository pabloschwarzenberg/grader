v1=int(input('numero1: '))
v2=int(input('numero2: '))
v3=int(input('numero3: '))

if v1<=v2<=v3:
    print(v1,v2,3)

elif v2<=v1<=v3:
    print(v2,',',v1,',',v3)
    
elif v3<=v2<=v1:
    print(v3,',',v2,',',v1)

elif v2<=v3<=v1:
    print(v2,',',v3,',',v1)
    
elif v1<=v3<=v2:
    print(v1,',',v3,',',v2)

elif v3<=v1<=v2:
    print(v3,',',v1,',',v2)
