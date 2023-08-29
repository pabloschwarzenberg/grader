#Factores Primos
a =int(2)
num=int(input("ingrese el numero entero"));
while (num != 1):
     if(num % a==0):
         print(str(a) + " ");
         num = num / a;
     else:
         a = a + 1     