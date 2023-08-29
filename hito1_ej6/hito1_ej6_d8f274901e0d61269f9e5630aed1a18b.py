#Digitar los números
x= eval(input("Digite el primer numero: "))
y= eval(input("Digite el segundo numero: "))
z= eval(input("Digite el tercer numero: "))

#Formula de los números
a=min(x,y,z)
c=max(x,y,z)
b= (x+y+z) - a - c 

#if y else
if(x==y==z):
  print(x,",",y,",",z)

else:
  if (x == y > z):
    print(z,",",x,",",y)

  else:
    if (x == y < z):
      print(x,",",y,",",z)

    else:
      if (y == z < x):
        print(y,",",z,",",x)

      else:
        if (y == z > x):
          print(x,",",y,",",z)

        else:
          if(x==z>y):
            print(y,",",x,",",z)

          else:
            if(x==z<y):
              print(x,",",z,",",y)

            else:

              print(a,",",b,",",c)