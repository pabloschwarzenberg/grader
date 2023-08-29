#Descomponer un número

n= input()

if(len(n)==4):
       a=n[0]
       b=n[1]
       c=n[2]
       d=n[3]
       print(a,"M+",b,"C+",c,"D+",d,"U")
   
elif(len(n)==3):
       a=n[0]
       b=n[1]
       c=n[2]
   
       print(a,"C+",b,"D+",c,"U")
elif(len(n)==2):
       a=n[0]
       b=n[1]
       print(a,"D+",b,"U")
elif(len(n)==1):
       a=n[0]

       print(a,"U")