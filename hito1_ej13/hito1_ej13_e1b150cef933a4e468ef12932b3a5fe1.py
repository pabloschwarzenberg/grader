#Factores Primos
p =int(2)
num=int(input());
while (num != 1):
     if(num % p==0):
         print(str(p) + " ");
         num = num / p;
     else:
         p = p + 1