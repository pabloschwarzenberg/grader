#Descomponer un número
n=eval(input("Ingresa un número de 4 cifras: "))

M=n//1000
C=(n-(M*1000))//100
D=(n-(M*1000)-(C*100))//10
U=(n-(M*1000)-(C*100)-(D*10))

print("Descompocición: %iM + %iC + %iD + %iU"%(M,C,D,U))
