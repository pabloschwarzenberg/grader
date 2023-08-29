#7_Cajero Automático nivel 2:
dinero=int(input("ingrese la cantidad de dinero:"))
queda=dinero//500
dinero=dinero%500
print(queda)
print(dinero)
lista=[500,200,100]
for i in lista:
    if dinero>=i:
        queda=dinero//i
        print(f"existen {str(queda)}billetes de ${str(i)}pesos")
        dinero=dinero %500

if dinero>500:
    queda=dinero//500
    print(f"existen {str(queda)} billetes de 500")
    dinero=dinero%500
if dinero>200:
    queda=dinero//200
    print(f"existen {str(queda)} billetes de 200")
    dinero=dinero%200
if dinero>100:
    queda=dinero//100
    print(f"existen {str(queda)} billetes de 100")
    dinero=dinero%100
