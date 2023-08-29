#Descomponer un número
x = int(input("ingrese numero="))
xs = str(x)
if(len(xs) <= 4 ):
    if(len(xs)== 4):
        print(xs[0:1] + "M +" + xs[1:2] + "C +" + xs[2:3] + "D +" + xs[3:4] + "U") 
        
    if(len(xs)== 3):
        print(xs[0:1] + "C +" + xs[1:2] + "D +" + xs[2:3] + "U")
    if(len(xs)== 2):
        print(xs[0:1] + "D +" + xs[1:2] + "U")
    if(len(xs)== 1):
        print(xs[0:1] + "U")
      