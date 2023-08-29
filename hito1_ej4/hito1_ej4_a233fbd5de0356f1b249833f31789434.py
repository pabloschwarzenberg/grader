#Conversión de Decimal a Binario
def BinDec(n)
    S=0
    i=0
    print('El binario',n)
    while(n>=1):
        d=n%10;
        S=S+d*pow(2,i);
        i=i+1
         
     print('corresponde al numero',S)
     
BinDec(1101)