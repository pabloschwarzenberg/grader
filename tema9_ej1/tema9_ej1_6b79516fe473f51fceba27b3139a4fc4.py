class Twitter:
    def __init__(self):
        self.trending_topics=[]

    def tweet(self,mensaje):
        if len(mensaje) > 140:
            return False
        aux = []
        mensaje_l = mensaje.split(" ")
        for word in mensaje_l:
            if word[0] == "#":
                aux.append(word[1:])
        print(aux, self.trending_topics)
        if aux:
            for element in aux:
                check = [x[0] == element for x in self.trending_topics]
                if not any(check):
                    self.trending_topics.append([element, 1])
                else: 
                    for i, wea in enumerate(self.trending_topics):
                        print(i, wea, element, wea[0])
                        if wea[0] == element:
                            print("lol")
                            index = i
                            break
                    self.trending_topics[index][1] += 1 
    
if __name__ == "__main__":
    twitter=Twitter()
    twitter.tweet("gano #laroja")
    twitter.tweet("grande #chile")
    twitter.tweet("#laroja con dos goles, le gano a brasil, grande #laroja")
    print(twitter.trending_topics)
           