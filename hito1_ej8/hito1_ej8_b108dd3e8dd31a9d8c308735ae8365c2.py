#Descomponer un número
a=int(input("ingrese un numero de 4 digitos como maximo:"))

if a>=0 and a<10:
    print("%xU"%(a))

elif a>=10 and a<100:
    w=str(a)
    y=w[0:1]
    z=w[1:2]
    print(y,"D +",z,"U")
    
elif a>=100 and a<1000:
    s=str(a)
    print(s[0:1],"C +",s[1:2],"D +",s[2:3],"U")
elif a>=1000 and a<10000:
    f=str(a)
    print(f[0:1],"M +",f[1:2],"C +",f[2:3],"D +",f[3:4],"U")
      