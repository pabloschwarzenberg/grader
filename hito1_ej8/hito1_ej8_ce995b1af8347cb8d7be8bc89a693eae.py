n=(input())
largo=len(n)
n=int(n)
if largo==1:
  print(n,'U')
if largo==2:
  print(n//10,'D+',n%10,'U')
if largo==3:
  print(n//100,'C+',(n//10)%10,'D+',n%10,'U')
if largo==4:
  print(n//1000,'M+',(n//100)%10,'C+',(n//10)%10,'D+',n%10,'U')