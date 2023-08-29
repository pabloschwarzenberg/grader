#Contestador de celular
x=int(input("ingrese numero telefonico de 8 digitos :"))
x=str(x)
a=int(x[0])
b=int(x[1])
c=int(x[2])
d=int(x[3])
e=int(x[4])
f=int(x[5])
g=int(x[6])
h=int(x[7])
hrs=int(input("ingrese la hora de la llamada :"))
if(hrs>=0 and hrs<=7):
    print("contestar")
if(hrs<=14 and f==9 and g==0 and h==9):
    print("contestar")
else:
    
    if(hrs<=14):
        print("no contestar")
        
    
if(hrs>=17 and hrs<=19):
    print("contestar")
    if(hrs>17 and hrs<19 and a==8 and b==7 and c==7):
        print("no contestar")
elif(hrs>19):
    print("no contestar")
      