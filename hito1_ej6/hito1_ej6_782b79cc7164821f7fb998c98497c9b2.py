num1=int(input('1er numero'))
num2=int(input('2do numero'))
num3=int(input('3er numero'))
if num1>num2 and num2>num3:
  print(num3,',',num2,',',num1)
elif num1<num2 and num2<num3: 
  print(num1,',',num2,',',num3)
elif num1<num3 and num2<num1: 
  print(num2,',',num1,',',num3)
elif num1>num3 and num3>num2: 
  print(num2,',',num3,',',num1)
elif num2>num1 and num1>num3: 
  print(num3,',',num1,',',num2)
elif num2>num3 and num3>num1: 
  print(num1,',',num3,',',num2)
elif num1==num2 and num2>num3:
  print(num3,',',num2,',',num1)
elif num1==num2 and num2<num3:
  print(num1,',',num2,',',num3)
elif num2==num3 and num1>num2:
  print(num3,',',num2,',',num1)
elif num2==num3 and num1<num2:
  print(num1,',',num2,',',num3) 
elif num1==num3 and num2>num1:
  print(num1,',',num3,',',num2) 
elif num1==num3 and num2<num1:
  print(num2,',',num3,',',num1) 
elif num1==num2==num3:
  print(num1,',',num2,',',num3)