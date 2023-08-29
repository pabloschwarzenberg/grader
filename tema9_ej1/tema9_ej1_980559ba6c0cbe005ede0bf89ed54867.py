class Twitter:
    def __init__(self):
        self.trending_topics=[]

    def tweet(self,mensaje):
        validar = False
        cantidad_c = len(mensaje)
        listaha = []
        if cantidad_c <= 140:
            lista = mensaje.split()
            for palabra in lista:
                for letra in palabra:
                    if letra == '#':
                        comprobacion = True
                        listaha.append(palabra)
                    elif letra != '#':
                        comprobacion = False
            validar = True
            self.trending_topics = listaha
        return print(listaha)  
        pass
    
if __name__ == "__main__":
    twitter=Twitter()
    twitter.tweet("gano #laroja")
    twitter.tweet("grande #chile")
    twitter.tweet("#laroja con dos goles, le gano a brasil, grande #laroja")
    print(twitter.trending_topics)

