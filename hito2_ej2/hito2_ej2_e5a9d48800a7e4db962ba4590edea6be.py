def secuenciacorrecta(sec):
    genoma = "actgACTG"
    secuencia=True
    while secuencia:
        for letra in sec:
            if letra in genoma:
                secuencia=True
            if letra not in genoma:
                secuencia=False
                break
        break
    if secuencia==True:
        print("correcta")
    if secuencia==False:
        print("incorrecta")
        

        
adn=input("ingrese secuencia de adn: ")
secuenciacorrecta(adn)


        
    
