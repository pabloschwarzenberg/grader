#Ordenar tres números
num=eval(input("ingrese un numero: "))
num2=eval(input("ingrese otro numero: "))
num3=eval(input("ingrese otro numero: "))
maxi=max(num,num2,num3)
mini=min(num,num2,num3)
medio=num+num2+num3-(maxi+mini)
print(mini,",",medio,",",maxi)      