#Factores Primos
z=int(2);
valor=eval(input("ingresa un numero: "))

while (valor !=1):
       if (valor % z ==0 ):
            print(str(z)+" ");
            valor=valor/z;
       else:
            z=z+1;