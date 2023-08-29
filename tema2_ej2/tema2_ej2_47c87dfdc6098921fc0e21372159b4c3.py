num=int()
num2=int()
suma = int(0);
for k in range(1,int(num/2)+1):
    if((num%k)==0):
        suma=suma+k
if suma==num2 and suma==num:
    print(True)
else:
    print(False) 
