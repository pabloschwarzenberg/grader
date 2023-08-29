SN=[]
I=0
while SN!=-1:
    N=int(input('ingrese número: '))
    if N==-1:
       break
    SN.append(N)
if len(SN)>0:
    print('cantidad=',len(SN))
    print('suma=',sum(SN))
    print('maximo=',max(SN))
else:
    print('cantidad=',len(SN))
    print('suma=',sum(SN))
    print('maximo=nd')
    