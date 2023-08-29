def divisores(numero):
i=1
divisores=[]
h=numero
while i<=numero:
if numero%i==0:
divisores.append(i)
numero=numero/i
i=i+1
if i>numero:
divisores.append(h)
else:
i=i+1
if divisores[-2]==divisores[-1]:
divisores.pop(-1)
return divisores

def suma_divisores(numero):
suma=[]
a=0
i=0
while i <len(numero):
a=a+numero[i]
i=i+1
        
return a   
    
def comparacion(numero,numerob,numeroc,numerod):
if numero==numerob and numeroc==numerod:
print("TRUE")
else:
print("FALSE")
        


numero1=int(input("numero 1: "))
numero2=int(input("numero 2: "))

divisores1=divisores(numero1)
divisores2=divisores(numero2)

suma1=suma_divisores(divisores1)
suma2=suma_divisores(divisores2)

respuesta=comparacion(numero1,suma2,numero2,suma1)
print(respuesta)
