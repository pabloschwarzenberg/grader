#Contestador de celular
nt=int(input("ingrese numero telefonico: "))
h=int(input("ingrese hora de la llamada: "))
n=(nt-nt%100000)/100000

if(0<=h<=7):
    print("Contestar")
elif(14<h<17):
    print("No contestar")
elif(7<h<14):
    if(nt%1000==909):
        print("Contestar")
    else:
        print("No contestar")
elif(17<h<19):
    if(n==877):
        print("No contestar")
    else:
        print("Contestar")
else:
    print("No contestar")