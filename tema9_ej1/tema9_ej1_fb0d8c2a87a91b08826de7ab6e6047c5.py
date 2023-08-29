class Twitter:
    def __init__(self):
        self.trending_topics = []

    def tweet(self, mensaje):
        self.mensaje = mensaje
        g = 0
        s = list(mensaje)
        contador=0
        while g < len(s):
            if s[g] == "#":
                espacio = mensaje[g:].find(" ")
                if espacio !=-1:
                    self.trending_topics.append(mensaje[g:espacio])
                    contador+=1
                else:
                    self.trending_topics.append(mensaje[g:])
                    contador+=1
            g = g + 1
        self.trending_topics=self.trending_topics[:2]
        return self.mensaje


  