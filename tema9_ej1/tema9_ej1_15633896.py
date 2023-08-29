
trendingtopics=[]
trendingtopics1=[]

class Twitter:
    def __init__(self):
        self.trending_topics=[]

    def tweet(self,mensaje):
        if len(mensaje)<=140:
            hashtags=[]
            todoshashtags=[]
            for caracter in mensaje:
                if caracter=="#":
                    hashtag=""
                    resto=mensaje[mensaje.find(caracter):len(mensaje)]
                    
                    for resto_caracteres in resto:
                       
        
                        if resto_caracteres!=" " and resto_caracteres!="/n":
                            hashtag=hashtag+resto_caracteres
                           
                        else:
                            break

                    todoshashtags.append(hashtag)
          
                    mensaje=mensaje.replace("#","1",1)

        for cada_hashtag in todoshashtags:
            trendingtopics.append(cada_hashtag)

        trendingtopics1=[]

        for cada_hashtag in trendingtopics:
            if cada_hashtag not in trendingtopics1:
                trendingtopics1.append(cada_hashtag)

            

        numerorepeticiones=[]

        for elementos in trendingtopics1:
            r=trendingtopics.count(elementos)

            numerorepeticiones.append(r)


        listatuplas=[]
   
        for i in range(len(numerorepeticiones)):
            tuplas=(numerorepeticiones[i],trendingtopics1[i])
            listatuplas.append(tuplas)


        listatuplas.sort()
        listatuplas.reverse()


        trending_topics_listo=[]

        for cadaelemento in listatuplas[0:3]:
 
            x1,x2=cadaelemento
           
            trending_topics_listo.append(x2)


        self.trending_topics=trending_topics_listo

if __name__ == "__main__":
    twitter=Twitter()
    twitter.tweet("gano #laroja")
    twitter.tweet("grande #chile")
    twitter.tweet("#laroja con dos goles, le gano a brasil, grande #laroja")
    print(twitter.trending_topics)
           