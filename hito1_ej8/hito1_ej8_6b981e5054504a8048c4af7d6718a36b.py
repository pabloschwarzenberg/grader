#Descomponer un número
valor = eval(input("Ingrese un numero: "))

M = (valor//1000)%10
C =(valor//100)%10
D = (valor//10)%10
U = (valor//1)%10

respuesta = print(str(M)+"M + "+str(C)+"C + "+str(D)+"D + "+str(U)+"U")      