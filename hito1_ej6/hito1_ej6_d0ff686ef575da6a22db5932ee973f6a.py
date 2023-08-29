#Ordenar tres números
print("Ingresa numeros")
n1=int(input("ingrese primer numero :"))
n2=int(input("ingrese segundo numero :"))
n3=int(input("ingrese tercer numero :"))


if n1 == n2 and n2 == n3:
    print('Los numeros ingresados son iguales : ')
    print(str(n1)+','+str(n2)+','+str(n3))
else:
    if n1<=n2 and n1<=n3:
        if n2<n3:
           print(str(n1)+','+str(n2)+','+str(n3))
        else:
           print(str(n1)+','+str(n3)+','+str(n2))
    else:
        if n2<=n1 and n2<=n3:
           if n1<n3:
              print(str(n2)+','+str(n1)+','+str(n3))
           else:
              print(str(n2)+','+str(n3)+','+str(n1))
        else:
           if n3<=n1 and n3<=n2:
              if n1<n2:
                 print(str(n3)+','+str(n1)+','+str(n2))
              else:
                 print(str(n3)+','+str(n2)+','+str(n1))

print("final del programa ..........")      