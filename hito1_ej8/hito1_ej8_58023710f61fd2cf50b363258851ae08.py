#Descomponer un número
n=eval(input("Ingrese un número de hasta 4 dígitos: "))
MM=n//1000
CC=(n-(M*1000))//100
DD=(n-(M*1000)-(C*100))//10
UD=(n-(M*1000)-(C*100)-(D*10))//1
MM=str(MM)
CC=str(CM)
DD=str(DD)
UU=str(UU)

M=str("M")
C=str("C")
D=str("D")
U=str("U")

mas=str("+")

print("MM+M+mas+CC+C+mas+DD+D+mas+UU+U")      