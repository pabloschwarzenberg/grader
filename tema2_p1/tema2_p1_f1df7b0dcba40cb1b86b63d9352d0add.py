# por favor escribe aquí tu función
def es_primo(contador):
    if(contador==1):
        return True
    else:
        return False
numero=int(input("numero:"))
divisor_candidato=2
contador=0
while (divisor_candidato<=numero):
    if (numero % divisor_candidato==0):
        contador+=1
    divisor_candidato=divisor_candidato+1
R=es_primo(contador)
if(R==True):
    print("True")
else:
    print("False")
