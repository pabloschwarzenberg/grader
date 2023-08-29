#Descomponer un número
n_1=int(input())
miles=n_1//1000
centena=(n_1//100-(miles*10))
decena=((n_1%100)-(n_1%10))//10
unidad=n_1%10
print(str(miles)+"M +" +str(centena)+ "C +" +str(decena)+"D  +"+str(unidad)+"U")    