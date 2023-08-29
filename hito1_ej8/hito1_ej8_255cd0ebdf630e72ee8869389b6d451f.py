#Descomponer un número
li = []
def mcdu(num):
  for i in num:
    li.append(int(i))
    print(li)

num1 = input("ingresa un numero de hasta 4 digitos: ")
mcdu(num1)
numa=num1[0:1]
numb=num1[1:2]
numc=num1[2:3]
numd=num1[3:4]
print(numa,"M",'+',numb,"C",'+',numc,"D",'+',numd,"U")



