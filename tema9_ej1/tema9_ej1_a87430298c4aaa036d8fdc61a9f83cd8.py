#El objetivo de este problema es implementar un prototipo de twitter, que aunque aún no te permitirá comunicarte con tus compañeros, servirá como base para que en el futuro puedas implementar esa funcionalidad. Tu programa debe:

#Aceptar los tweets del usuario, limitados a 140 caracteres.
#Permitir el ingreso de #hashtags, creados por la persona, los cuales deben almacenarse en una lista, junto con el número de veces que han sido mencionados.
#Mostrar los tres hashtag más repetidos hasta el momento.

class Twitter:
    def __init__(self):
        self.trending_topics=[]

    def tweet(self,mensaje):
        hashtags=[palabra for palabra in mensaje.split() if palabra.startswith("#")]
        for hashtag in hashtags:
            if hashtag in [t[0] for t in self.trending_topics]:
                index=[t[0] for t in self.trending_topics].index(hashtag)
                self.trending_topics[index][1]+=1
            else:
                self.trending_topics.append([hashtag,1])
        self.trending_topics.sort(key=lambda x:x[1],reverse=True)
        if len(self.trending_topics)>3:
            self.trending_topics=self.trending_topics[:3]
    
if __name__ == "__main__":
    twitter=Twitter()
    twitter.tweet("gano #laroja")
    twitter.tweet("grande #chile")
    twitter.tweet("#laroja con dos goles, le gano a brasil, grande #laroja")
    print(twitter.trending_topics)