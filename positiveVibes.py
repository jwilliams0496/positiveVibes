from twython import Twython

searchSize = 20

def main():
    user = input("Type the username of any Twitter user: ")
    getNumPos(user)

# open the file of all positive words, and return a list of them
def getCompareWords():
    file = open("positiveWords.txt", "r")
    return file.read().split();
    
# Let's not push my API keys to github lol
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

def getNumPos(user):
    username = user;
    
    accessToken = getKeys()[0]
    accessTokenSecret = getKeys()[1]
    consumerKey = getKeys()[2]
    consumerSecret = getKeys()[3]
    
    print("Obtaining OAuth 2 token\n\n")
    
    twitter = Twython(consumerKey, consumerSecret, oauth_version=2)
    ACCESS_TOKEN = twitter.obtain_access_token()
    
    print("Access token granted\n")
    
    twitter = Twython(consumerKey, access_token=ACCESS_TOKEN)
    userTimeline = twitter.get_user_timeline(screen_name = username, count = searchSize)
        
    posWords = getCompareWords();
    score = 0;

    print("\n\nTweets from ", username, "\n\n")
        
    # And print the tweets for that user.
    for tweet in userTimeline:
        print(tweet['text'] + "\n")
        for i, word in enumerate(tweet['text'].split()):
            if word.lower() in posWords:
                score += 1
    
    print(str(score) + " positive words in " + str(searchSize) + " previous tweets!")
    rateScore(score);
    
def rateScore(score):
    positivity = score - searchSize
    
    if positivity < -15:
        print("Uh oh, this user is not very positive!")
    if positivity >= -15 and positivity < -7:
        print("This user looks very neutral.")
    if positivity >= -7 and positivity < 15:
        print("This user gives off some good vibes")
    if positivity >= 15 and positivity < 30:
        print("This user has lots of positive energy!")
    if positivity >= 30 and positivity < 45:
        print("This user is incredibly positive!")
    if positivity >= 45:
        print("WOW, this user is amazing!")
    
    
main()