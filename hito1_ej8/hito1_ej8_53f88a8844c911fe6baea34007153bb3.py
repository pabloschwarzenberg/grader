#Descomponer un número
number=str(input("Número: "))
digitos=[]
for x in number:
    digitos.append(x)

if len(digitos)==4:
    print(digitos[0]+"M","+",digitos[1]+"C","+",digitos[2]+"D","+",digitos[3]+"U")
elif len(digitos)==3:
    print(digitos[0]+"C","+",digitos[1]+"D","+",digitos[2]+"U")
elif len(digitos)==2:
    print(digitos[0]+"D","+",digitos[1]+"U")
elif len(digitos)==1:
    print(digitos[0]+"U")