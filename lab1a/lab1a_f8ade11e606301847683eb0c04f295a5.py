print("Resultados ELECCIONES 2K19","\n")
comuna1=float(input("Ingresa el Total de Votantes de la COMUNA 1: "))
print("")
comuna2=float(input("Ingresa el Total de Votantes de la COMUNA 2: "))
print("")
comuna3=float(input("Ingresa el Total de Votantes de la COMUNA 3: "))
print("")
votos_comuna1=int(input("Ingresa los Votos de la COMUNA 1: "))
print("")
votos_comuna2=int(input("Ingresa los Votos de la COMUNA 2: "))
print("")
votos_comuna3=int(input("Ingresa los Votos de la COMUNA 3: "))
print("")
def a(votos_comuna1,votos_comuna2,votos_comuna3):
    if votos_comuna1>=comuna1*0.8 or votos_comuna2>=comuna2*0.8 or votos_comuna3>=comuna3*0.8:
        print("Resultado: SENADORA SELECTA","\n")
    elif votos_comuna1<=comuna1*0.8 or votos_comuna2<=comuna2*0.8 or votos_comuna3<=comuna3*0.8:
        print("Resultado: CANDIDATA PERDEDORA","\n")
def b(votos_comuna1,votos_comuna2,votos_comuna3):
    if votos_comuna1+votos_comuna2>=(comuna1+comuna2)*0.7 or votos_comuna1+votos_comuna3>=(comuna1+comuna3)*0.7 or votos_comuna2+votos_comuna3>=(comuna2+comuna3)*0.7:
        print("Resultado: SENADORA SELECTA","\n")
    elif votos_comuna1+votos_comuna2<=(comuna1+comuna2)*0.7 or votos_comuna1+votos_comuna3<=(comuna1+comuna2)*0.7 or votos_comuna2+votos_comuna3<=(comuna1+comuna2)*0.7:
        print("Resultado: CANDIDATA PERDEDORA","\n")
def c(votos_comuna1,votos_comuna2,votos_comuna3):
    if votos_comuna1+votos_comuna2+votos_comuna3>=(comuna1+comuna2+comuna3)*0.4:
        print("Resultado: SENADORA SELECTA","\n")
    elif votos_comuna1+votos_comuna2+votos_comuna3<=(comuna1+comuna2+comuna3)*0.4:
        print("Resultado: CANDIDATA PERDEDORA","\n")
a(votos_comuna1,votos_comuna2,votos_comuna3)
b(votos_comuna1,votos_comuna2,votos_comuna3)
c(votos_comuna1,votos_comuna2,votos_comuna3)

        print("Resultado: CANDIDATA PERDEDORA","\n")