#Descomponer un número
a=input()
if len(a)==3:
   a="0"+a
elif len(a)==2:
   a="0"+"0"+a
elif len(a)==1:
   a="0"+"0"+"0"+a
b=str(a)[0]
c=str(a)[1]
d=str(a)[2]
e=str(a)[3]
print(b,"M+",c,"C+",d,"D+",e,"U")