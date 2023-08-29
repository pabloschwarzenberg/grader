#Descomponer un número
# 1 2 3 4
num=eval(input(''))
if num>=1000 and num<=9999:
  n1=num//1000
  n2=(num//100)%10
  n3=(num%100)//10
  n4=num%10
  print(n1,str('M'),'+',n2,str('C'),'+',n3,str('D'),'+',n4,str('U'))
elif num>=100 and num<=999:
  n1=(num//100)%10
  n2=(num%100)//10
  n3=num%10
  print(n1,str('C'),'+',n2,str('D'),'+',n3,str('U'))
elif num>=10 and num<=99:
  n1=(num%100)//10
  n2=num%10
  print(n1,str('D'),'+',n2,str('U'))
elif num>1 and num<9:
  n1=num%10
  print(n1,str('U'))  
