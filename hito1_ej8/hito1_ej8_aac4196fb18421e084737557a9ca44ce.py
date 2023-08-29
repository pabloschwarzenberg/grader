#Descomponer un número
n = input("ingrese un número de hasta 4 cifras : ")
if(len(n)>4 or len(n)<0):
    print("numero mal ingresado")
else:
    if(len(n)==4):
        print(n[0],"M","+",n[1],"C","+",n[2],"D","+",n[3],"U")
    elif(len(n)==3):
        print(n[0],"C","+",n[1],"D","+",n[2],"U")
    elif(len(n)==2):
        print(n[0],"D","+",n[1],"U")
    elif(len(n)==1):
        print(n[0],"U")    