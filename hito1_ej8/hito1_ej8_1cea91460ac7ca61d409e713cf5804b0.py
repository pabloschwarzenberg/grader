#Descomponer un número
x=input()
if len(x)>=4:
  print(x[:1]+"M","+",x[1:2]+"C","+",x[2:3]+"D","+",x[3:4]+"U")
if 3<=len(x)<4:
  print(x[:1]+"C","+",x[1:2]+"D","+",x[2:3]+"U")
if 2<=len(x)<3:
  print(x[:1]+"D","+",x[1:2]+"U")
if len(x)<2:
  print(x[:1]+"U")
  