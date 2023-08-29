class Twitter:
    def __init__(self):
        self.trending_topics=[]

    def tweet(self,mensaje):
        # Validar que el mensaje no supere los 140 caracteres
        if len(mensaje) > 140:
            return # Retornar sin hacer nada si el mensaje es muy largo
        # Buscar los hashtags en el mensaje usando una expresión regular
        import re
        hashtags = re.findall("#\w+", mensaje)
        # Recorrer los hashtags encontrados con un ciclo for
        for hashtag in hashtags:
            # Buscar el hashtag en la lista de trending topics
            encontrado = False # Variable para indicar si se encontró el hashtag
            for topic in self.trending_topics:
                # Si se encuentra el hashtag, aumentar su contador en uno
                if topic[0] == hashtag:
                    topic[1] += 1
                    encontrado = True # Cambiar la variable a True
                    break # Salir del ciclo interno
            # Si no se encuentra el hashtag, agregarlo a la lista con contador uno
            if not encontrado:
                self.trending_topics.append([hashtag, 1])
        # Ordenar la lista de trending topics de mayor a menor según el contador
        self.trending_topics.sort(key=lambda x: x[1], reverse=True)
        # Mostrar los tres primeros elementos de la lista, si los hay
        print("Los tres hashtags más repetidos son:")
        for i in range(min(3, len(self.trending_topics))):
            print(self.trending_topics[i][0], "con", self.trending_topics[i][1], "menciones")
    
if __name__ == "__main__":
    twitter=Twitter()
    twitter.tweet("gano #laroja")
    twitter.tweet("grande #chile")
    twitter.tweet("#laroja con dos goles, le gano a brasil, grande #laroja")
    print(twitter.trending_topics)
