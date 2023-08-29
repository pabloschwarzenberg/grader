string=input()
n=int(input())
if len(string)<n:
   print("ninguna")
else:
   a=0
   while a!=len(string):
     if  a==len(string):
       break
     frase=string[a:a+n]
     print(frase)
     a=a+n
   