import praw, json

bot = praw.Reddit(user_agent='theBottyBot',
                client_id='PC7DHwT8m1ji-g',
                client_secret='1H9HZgWMBD3Ofmy1uYSV2SRu7V8',
                username='gitKlone',
                password='T562ndu2b723b')

subreddit = bot.subreddit('allmywut')
comments = subreddit.stream.comments()
#read json
with open('data.json') as json_data: data = json.load(json_data)

CHECK = ['eJwBswBM/zEwADE2MgBDeXBoZXJ0ZXh0LE2jxJS1EzMc80kOK+hra1GKnXgQKQgVitIy8NgA7kxn','dfghjkl']


for comment in comments:
    text = comment.body # Fetch body
    author = comment.author # Fetch author

    if author not in data:
        data[author] = [[], 0]
    z = 0
    for words in range(len(CHECK)):

        CHECKs = [z]
        z += 1
        if CHECKs in text and text not in data[author][0] and data[author][1] != 3:

            #Add comment to list of comments they have made
            data[author][0].append(text)
            #Add strike
            data[author][1] += 1
            #Strikes left
            strikesLeft = 3 - data[author][1]
            # Generate a message
            message = "Hello user " + str(author) + ", you have " + str(strikesLeft) + " strikes left until you will be reported!".format(author)
            comment.reply(message) # Send message

    if data[author][1] == 3:

        #REPORT USER HERE
        message = "Hello user " + str(author) + ", you have been reported!".format(author)
        comment.reply(message) # Send message

#save json
with open('data.json', 'w') as json_data: json.dump(data, json_data)


#To run: python3 redditBot1.py
