def viewHastag(text):
    u = text.split()
    hastags = []
    for i in range(len(u)):
        if u[i][0] == "#" and u[i] not in hastags:
            hastags.append(u[i])
    return hastags

def get_count_list(lista):
    u = []
    marked = []
    for i in range(len(lista)):
        if lista[i] not in marked:
            counter = lista.count(lista[i])
            u.append([lista[i],counter])
            marked.append(lista[i])
    return u

class Tweet:
    def __init__(self,text):
        self.text = text
        self.hashtag = viewHastag(text)

class Twitter:
    def __init__(self):
        self.trending_topics = []
        self.all_tweets = []
        self.hashtag_counts = []

    def tweet(self, text):
        if len(text) > 140:
            print("El texto es muy grande")
        else:
            new_tweet = Tweet(text)
            self.all_tweets.append(new_tweet)

    def get_trending_topics(self):
        raw_hashtags = []
        for tweet in self.all_tweets:
            for hashtag in tweet.hashtag:
                raw_hashtags.append(hashtag)
                
        self.hashtag_counts = get_count_list(raw_hashtags) 
        self.hashtag_counts = sorted(self.hashtag_counts, key = lambda x : x[1], reverse = True)

        u = 0
        for i in range(len(self.hashtag_counts)):
            if u == 3:
                break
            self.trending_topics.append(self.hashtag_counts[i][0])
            u += 1
            
    
if __name__ == "__main__":
    twitter=Twitter()
    twitter.tweet("gano #laroja")
    twitter.tweet("grande #chile")
    twitter.tweet("#laroja con dos goles, le gano a brasil, grande #laroja")
    twitter.get_trending_topics()
    print(twitter.hashtag_counts)
    print(twitter.trending_topics)