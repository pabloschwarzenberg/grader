#Contestador de celular
z="CONTESTAR"
x="NO CONTESTAR"
y=str(input(print("el numero que llama")))
h=int(input(print("hora de la llamada(de 0 a 23)")))
if(int(y[7])==9):
    print("hola")
if(h>=0 and h<=7):
    print(z)
elif(h<14 and int(y[5])==9 and int(y[6])==0 and int(y[7])==9):
    print(z)
elif(int(y[0])==8 and int(y[1])==7 and int(y[2])==7):
    print(x)
elif(h>=17 and h<=19):
    print(z)
else:
    print(x)