#Descomponer un númer
A=int(input())
unidadesA=(A%10)
decenasA=(A//10)
decenasA2=(decenasA%10)
centenasA=(A//100)
centenasA2=(centenasA%10)
milA=(A//1000)
print(str(milA)+"M+"+str(centenasA2)+"C+"+str(decenasA2)+"D+"+str(unidadesA)+"U")