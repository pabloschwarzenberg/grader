numero=int(input("Ingrese su numero: "))
numerodereserva=numero

Um=int(numero/1000)
numerodereserva=numero%1000

Uc=int(numerodereserva/100)
numerodereserva=numero%100

Ud=int(numerodereserva/10)
numerodereserva=numero%10

U=int(numerodereserva/1)

if Um>0:
    print(Um,"M+",Uc,"C+",Ud,"D+",U,"U")
elif Uc>0:
    print(Uc, "C+", Ud, "D+", U, "U")
elif Ud>0:
    print(Ud, "D+", U, "U")
else:
    print(U,"U")