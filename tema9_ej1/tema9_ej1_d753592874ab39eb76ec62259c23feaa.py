class Twitter:
    def __init__(self):
        self.trending_topics=[]

    def tweet(self,mensaje):
        contador=0
        for letra in mensaje:
            contador+=1
        if contador>140:
            return False
        else:
            mensaje=mensaje.replace(","," ")
            #"".join(mensaje)
            #mensaje=mensaje.split(" ")            
            a=0
            lista=[]
            lista_chica=["",""]
            mensaje=mensaje.split(" ")
            #print(mensaje)
            for palabra in mensaje:
                #print(palabra)
                b=[]
                if len(palabra)>0 and palabra[0]=="#":
                    #print(palabra)
                    #lista_chica[0]=palabra
                    b.append(palabra)
                    a=mensaje.count(palabra)
                    b.append(a)
                    #lista_chica[1]=a
                    if b not in self.trending_topics:
                        self.trending_topics.append(b)
                        lista_chica[0]=""
                        lista_chica[1]=""
            lista=self.trending_topics.sort(key=lambda elemento: elemento[1], reverse=True)
            return lista
                        
if __name__ == "__main__":
    twitter=Twitter()
#    twitter.tweet("gano #laroja")
#    twitter.tweet("grande #chile")
    print(twitter.tweet("al continuar con #laroja con dos goles, le gano a brasil, grande #laroja"))
    print(twitter.tweet("#laroja con #lindo dos goles, grande #chile le #lindo gano #lindo a brasil, grande #laroja "))
    #print(twitter.trending_topics)
