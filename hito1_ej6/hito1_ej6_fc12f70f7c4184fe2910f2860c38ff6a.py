valor= eval(input("ingrese un valor cualquiera: "))
valor2=eval(input("ingrese un segundo valor: "))
valor3=eval(input("ingrese un tercer valor: "))
if valor<valor2<valor3:
    menor=valor
    medio=valor2
    mayor=valor3
    print(menor,",",medio,",",mayor)
else:
    if valor<valor2>valor3 and valor<valor3:
        menor=valor
        medio=valor3
        mayor=valor2
        print(menor,",",medio,",",mayor)
    else:
        if valor<valor2>valor3 and valor>valor3:
            menor=valor3
            medio=valor
            mayor=valor2
            print(menor,",",medio,",",mayor)
        else:
            if valor>valor2>valor3:
                menor=valor3
                medio=valor2
                mayor=valor
                print(menor,",",medio,",",mayor)
            else:
                if valor>valor2<valor3 and valor>valor3:
                    menor=valor2
                    medio=valor3
                    mayor=valor
                    print(menor,",",medio,",",mayor)
                else:
                    if valor>valor2<valor3 and valor<valor3:
                        menor=valor2
                        medio=valor
                        mayor=valor3
                        print(menor,",",medio,",",mayor)
                    else:
                        if valor<valor2>valor3 and valor>valor3:
                            menor=valor3
                            medio=valor
                            mayor=valor2
                            print(menor,",",medio,",",mayor)
                        else:
                            if valor==valor2<valor3:
                                menor=valor
                                medio=valor2
                                mayor=valor3
                                print(menor,",",medio,",",mayor)
                            else:
                                if valor==valor2>valor3:
                                    menor=valor3
                                    medio=valor
                                    mayor=valor2
                                    print(menor,",",medio,",",mayor)
                                else:
                                    if valor<valor2==valor3:
                                        menor=valor
                                        medio=valor2
                                        mayor=valor3
                                        print(menor,",",medio,",",mayor)
                                    else:
                                        if valor>valor2==valor3:
                                            menor=valor2
                                            medio=valor3
                                            mayor=valor
                                            print(menor,",",medio,",",mayor)
                                        else:
                                            if valor<valor2>valor3 and valor==valor3:
                                                menor=valor
                                                medio=valor3
                                                mayor=valor2
                                                print(menor,",",medio,",",mayor)
                                            else:
                                                if valor==valor2==valor3:
                                                    menor=valor
                                                    medio=valor2
                                                    mayor=valor3
                                                    print(menor,",",medio,",",mayor)
                                                else:
                                                    menor=valor2
                                                    medio=valor
                                                    mayor=valor3
                                                    print(menor,",",medio,",",mayor)
                                                
                                                
