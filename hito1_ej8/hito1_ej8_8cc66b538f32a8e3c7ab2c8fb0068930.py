#Descomponer un número
x=int(input("Número: "))

print(str(x//1000)+"M", " + ", str((x//100)%10)+"C", " + ", str((x//10)%10)+"D", " + ", str(x%10)+"U")