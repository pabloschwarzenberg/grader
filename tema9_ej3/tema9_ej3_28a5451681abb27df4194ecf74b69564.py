def decodificar(mensaje):
    a=str(mensaje[0:8])
    decimal=(int(str(a),2))
    letral=chr(decimal)
    
    b=str(mensaje[10:17])
    decimal2=int(str(b),2)
    letral2=chr(decimal2)
    
    g=str(mensaje[19:26])
    decimal3=(int(str(g),2))
    letral3=chr(decimal3)

    d=str(mensaje[28:35])
    decimal4=(int(str(d),2))
    letral4=chr(decimal4)
    palabra= letral+letral2+letral3+letral4
    return palabra
if __name__ == "__main__":
    mensaje=decodificar("01101000,01101111,01101100,01100001")
    print(mensaje)
         