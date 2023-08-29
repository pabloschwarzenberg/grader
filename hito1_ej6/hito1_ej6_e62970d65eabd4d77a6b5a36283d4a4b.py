a = int(input("Ingrese el primer número"))
b = int(input("Ingrese el segundo número"))
c = int(input("Ingrese el tercer número"))

if(a>b and a>c):
    if(b>c):
        print(c," , ",b," , ",a) 
    else:
        print(b," , ",c," , ",a) 

if(b>a and b>c):
    if(a>c):
        print(c," , ",a," , ",b) 
    else:
        print(a," , ",c," , ",b) 

if(c>a and c>b):
    if(a>b):
        print(b," , ",a," , ",c) 
    else:
        print(a," , ",b," , ",c) 