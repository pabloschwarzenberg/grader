#Descomponer un número
n=int(input())

if n>=1000 :
  print(n//1000,"M +",(n//100)%10,"C +",(n//10)%10,"D +",(n//1)%10,"U")
elif n>=100 :
  print((n//100)%10,"C +",(n//10)%10,"D +",(n//1)%10,"U")
elif n>=10 :
  print((n//10)%10,"D +",(n//1)%10,"U")
else:
  print((n//1)%10,"U")