n_1=eval(input("ingrese el primer numero: "))
n_2=eval(input("ingrese el segundo numero: "))
n_3=eval(input("ingrese el tercer numero: "))

if((n_1<=n_2) and (n_1<=n_3)):
         
    menor=n_1
    if (n_2<=n_3):
         medio=n_2
         mayor=n_3

    else:
         medio=n_3
         mayor=n_2

elif((n_2<=n_1) and (n_2<=n_3)):
     menor=n_2
     if (n_1<=n_3):
      medio=n_1
      mayor=n_3
     else:
      medio=n_3
      mayor=n_1

else:
    menor=n_3
    if ((n_1<=n_2)):
        medio=n_1
        mayor=n_2
    else:
        medio=n_2
        mayor=n_1

print(str(menor)," ,",str(medio),", ",str(mayor))