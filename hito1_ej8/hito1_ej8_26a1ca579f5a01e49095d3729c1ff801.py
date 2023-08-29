#Descomponer un número
num=input('ingrese numero: ')
if len(num)==1:
    print(num[0],'U')

if len(num)==2:
    print(num[0],'D','+',num[1],'U')

if len(num)==3:
    print(num[0],'C','+',num[1],'D','+',num[2],'U')

if len(num)==4:
    print(num[0],'M','+',num[1],'C','+',num[2],'D','+',num[3],'U')