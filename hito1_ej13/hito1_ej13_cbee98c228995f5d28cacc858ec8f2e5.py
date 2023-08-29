#Factores Primos
TNum=int(input('Ingresa un número'))
CoNum=TNum
L_Fact=[]

TC=2
while CoNum!=1:
    if CoNum%TC==0:
        L_Fact.append(TC)
        CoNum=(CoNum/TC)
        TC=2
    else:
        TC=TC+1

i=0
while i<=(len(L_Fact)-1):
    print(L_Fact[i],end='\n')
    i=i+1