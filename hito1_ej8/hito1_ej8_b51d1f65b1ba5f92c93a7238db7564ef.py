#Descomponer un número
num = int(input("Ingrese un valor de 4 cifras "))
m = (num-(num%1000))/1000
res = num%1000
c = (res-(res%100))/100
res=res%100
d = (res-(res%10))/10
u = res%10
print("El valor descompuesto quedaría como: ",m,"M +""",c,"C +",d,"D +",u,"U")
