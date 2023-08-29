decimal=int(input('escriba un decimal: '))
binario=[]
while decimal != 1:
    if int(decimal)==0:
        break
    if int(decimal)%2==0:
        binario.append(0)
    if int(decimal)%2!=0:
        binario.append(1)
        
    decimal=int(decimal)/2
if decimal==1:
    binario.append(1)
for i in reversed(binario):
    print(i,end='')