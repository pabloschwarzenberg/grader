num=input()
largo=len(num)
M="M"
C="C"
D="D"
U="U"
if largo==1:
  print(num[0]+U)
if largo==2:
  print(num[0]+D,"+",num[1]+U)
if largo==3:
  print(num[0]+C,"+",num[1]+D,"+",num[2]+U)
if largo==4:
 print(num[0]+M,"+",num[1]+C,"+",num[2]+D,"+",num[3]+U)
