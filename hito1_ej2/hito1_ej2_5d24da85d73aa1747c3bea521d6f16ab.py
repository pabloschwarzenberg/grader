#Contestador de celular
n=int(input())
h=int(input())
x1=(n//1000)*1000
x2=(n//100000)
z= n-x1
if 0<=h<=7:
  print("CONTESTAR")
elif (17<h<19 and x2==877):
  print("NO CONTESTAR") 
elif (7<h<14 and z==909) or (14<h<19):
        print("CONTESTAR")
else: 
  print("NO CONTESTAR")