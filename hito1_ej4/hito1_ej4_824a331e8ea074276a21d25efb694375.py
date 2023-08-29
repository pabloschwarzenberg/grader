#Conversión de Decimal a Binario
re=""
a= int(input("ingrese un numero:"))
#for i in range(20):
sobra=a
while sobra >=1:
   resto=sobra%2
   #print(sobra)
   if resto==0:
     bi=0
   else:
     bi=1  
   sobra=sobra//2    
   re=re+str(bi)

#print(resultado)
l=len(re)
for i in range(l):
   resultado=re[::-1]
        
print("resultado=",resultado)  

   