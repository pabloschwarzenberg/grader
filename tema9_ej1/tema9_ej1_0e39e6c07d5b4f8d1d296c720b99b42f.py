class Twitter:
    def _init_(self,trending_topics):
        self.trending_topics=trending_topics

    def tweet(self,mensaje):
        mensaje_lista=mensaje.split(" ")
        i=0
        if len(mensaje)<=140:
            while i<len(mensaje_lista):
                if mensaje_lista[i][0]=="#":
                    if not mensaje_lista[i] in self.trending_topics:
                        self.trending_topics.append(mensaje_lista[i])
                i+=1