topics={}
class Twitter:
    def __init__(self):
        self.trending_topics=[]
    def tweet(self,mensaje):
        if len(mensaje)<=140:
            pos=0
            global topics
            for i in mensaje:
                if i=='#':
                    hashtag=''
                    pos_2=pos
                    while True:
                        if pos_2<len(mensaje):
                            if mensaje[pos_2]!=' ':
                                hashtag=hashtag+mensaje[pos_2]
                                pos_2+=1
                            
                            else:
                                if hashtag in topics:
                                    topics[hashtag]+=1
                                else:
                                    topics[hashtag]=1
                                break
                        else:
                            if hashtag in topics:
                                topics[hashtag]+=1
                            else:
                                topics[hashtag]=1
                            break
                pos+=1
            for i in topics:
                final=[]
                topics_1=topics.copy()
                lista=list(topics_1.values())
                lista.sort()
                lista.reverse()
                for i in lista:
                    for j in topics_1:
                        if i==topics_1[j]:
                            final.append(j)
                            del topics_1[j]
                            break
            self.trending_topics=final[0:3]
            
        else:
            return False
    
if __name__ == "__main__":
    twitter=Twitter()
    twitter.tweet("gano #laroja")
    twitter.tweet("grande #chile")
    twitter.tweet("#laroja con dos goles, le gano a brasil, grande #laroja")
    print(twitter.trending_topics)
           