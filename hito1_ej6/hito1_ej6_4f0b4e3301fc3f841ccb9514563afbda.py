n=int(input('Ingrese Numero: '))
n2=int(input('Ingrese Numero: '))
n3=int(input('Ingrese Numero: '))

if n<=n2 and n2<=n3:
    print(str(n)+','+str(n2)+','+str(n3))
else:
    if n<=n3 and n3<=n2:
        print(str(n)+','+str(n3)+','+str(n2))
    else:
        if n2<=n and n<=n3:
            print(str(n2)+','+str(n)+','+str(n3))
        else:
            if n2<=n3 and n3<=n:
                print(str(n2)+','+str(n3)+','+str(n))
            else:
                if n3<=n and n<=n2:
                    print(str(n3)+','+str(n)+','+str(n2))
                else:
                    if n3<=n2 and n2<=n:
                        print(str(n3)+','+str(n2)+','+str(n))

        
