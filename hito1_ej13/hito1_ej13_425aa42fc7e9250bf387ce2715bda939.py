#Factores Primos
#para descomponer un numero y decir los factores primos
div =int(2)
num = int(input("favor ingrese un numero: "))
while (num!=1):
    if(num% div==0):
        print(str(div)+"");
        num = num / div;
    else:
        div=div+1;