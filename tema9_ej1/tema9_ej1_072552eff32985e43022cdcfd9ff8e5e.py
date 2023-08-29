def funcion_ordenamiento(item):
    return item[1]

class Twitter:
    def __init__(self):
        self.trending_topics=[]

    def tweet(self,mensaje):
        if len(mensaje)>140:
            return False
        else:
            #con esto vemos si el tweet contiene un hashtag
            pos=mensaje.find("#")
            while pos!=-1:
                fin=mensaje.find(" ",pos)
                if fin==-1:
                    hashtag=mensaje[pos:]
                    mensaje=""
                else:
                    hashtag=mensaje[pos:fin]
                    mensaje=mensaje[fin:]
                #revisamos si el hashtag ya está en el listado
                existe=False
                for topic in self.trending_topics:
                    if topic[0]==hashtag:
                        topic[1]=topic[1]+1
                        existe=True
                        break
                #si no está lo agregamos
                if not existe:
                    self.trending_topics.append([hashtag,1])
                pos=mensaje.find("#")
            #con esta función ordenamos la lista de trending topics de mayor a menor
            self.trending_topics=sorted(self.trending_topics,key=funcion_ordenamiento,reverse=True)
        return self.trending_topics

if __name__ == "__main__":
    twitter=Twitter()
    twitter.tweet("gano #laroja")
    twitter.tweet("grande #chile")
    twitter.tweet("#laroja con dos goles, le gano a brasil, grande #laroja")
    print(twitter.trending_topics)
           