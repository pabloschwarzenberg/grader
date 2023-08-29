class Twitter:
    def __init__(self):
        self.trending_topics=[]

    def tweet(self,mensaje):
        caracteres = 0
        for caracter in mensaje:
            if not caracter = " ":
               caracteres+=1
        if caracteres>140:
             return "Número inválido de caracteres"
        else:
             hashtags = []
             hashtag = 0
             for palabra in mensaje:
                 if "#" in palabra:
                     hashtags.append(palabra)
                     hashtag+=1
             lista_1 = []
             lista_2 = []
             lista_3 = []
             for i in range(len(hashtags)):
     
                     
             
             
           
        
            
    
if __name__ == "__main__":
    twitter=Twitter()
    twitter.tweet("gano #laroja")
    twitter.tweet("grande #chile")
    twitter.tweet("#laroja con dos goles, le gano a brasil, grande #laroja")
    print(twitter.trending_topics)
           