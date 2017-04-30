from twython import Twython

username = "JonTronShow"
serachSize = 100

def getCompareWords():
    pass

def getKeys():
    file = open("APIKeys.txt" , "r")
    
    accessToken = file.readline()
    accessToken = accessToken.strip('\n')
    
    accessTokenSecret = file.readline()
    accessTokenSecret = accessTokenSecret.strip('\n')
    
    consumerKey = file.readline()
    consumerKey = consumerKey.strip('\n')
    
    consumerSecret = file.readline()
    consumerSecret  = consumerSecret.strip('\n')
    
    return accessToken, accessTokenSecret, consumerKey, consumerSecret

def main():
    accessToken = getKeys()[0]
    accessTokenSecret = getKeys()[1]
    consumerKey = getKeys()[2]
    consumerSecret = getKeys()[3]
    
    print("Obtaining OAuth 2 token\n\n")
    
    twitter = Twython(consumerKey, consumerSecret, oauth_version=2)
    ACCESS_TOKEN = twitter.obtain_access_token()
    
    print("Access token granted\n")
    
    twitter = Twython(consumerKey, access_token=ACCESS_TOKEN)
    userTimeline = twitter.get_user_timeline(screen_name = username)
        
    print("\n\nTweets from ", username, "\n\n")
        
    # And print the tweets for that user.
    for tweet in userTimeline:
        print(tweet['text'] + "\n\n")
        
        for word in tweet['tweet']:
            pass
    
main()