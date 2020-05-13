class Twitter:
    
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.news_dict = {}
        self.news_ls = []
        self.follow_dict = {}
        

    def postTweet(self, userId, tweetId):
        """
        Compose a new tweet.
        发一条twitter时，将自己加为好友
        """

        if userId not in self.follow_dict.keys():
            self.follow_dict[userId] = [userId]            

        if userId not in self.news_dict.keys():
            self.news_dict[userId] = [tweetId]
        else:
            self.news_dict[userId].append(tweetId)
        
        self.news_ls.append([userId,tweetId])


    def getNewsFeed(self, userId):
        """
        Retrieve the 10 most recent tweet ids in the user's news feed. Each item in the news feed must be posted by users who the user followed or by the user herself. Tweets must be ordered from most recent to least recent.
        """
        # print(self.follow_dict)

        recent_news_ls = []
        n = 0
        for u,i in self.news_ls[::-1]:
            # print(u,i)
            if (u in self.follow_dict[userId]) & (n<=9):
                recent_news_ls.append(i)
                n += 1
            else:
                continue
        
        print(recent_news_ls)
        return recent_news_ls
        

    def follow(self, followerId, followeeId):
        """
        Follower follows a followee. If the operation is invalid, it should be a no-op.
        将自己的id加为自己好友，可以在最近twitter里找到
        """            
        
        if followerId not in self.follow_dict.keys():
            self.follow_dict[followerId] = [followerId]
            self.follow_dict[followerId].append(followeeId)
        else:
            self.follow_dict[followerId].append(followeeId)
        

    def unfollow(self, followerId, followeeId):
        """
        Follower unfollows a followee. If the operation is invalid, it should be a no-op.
        自己好友不会剔除自己
        """
        if followeeId == followerId:
            return self.follow_dict[followerId]
        if followeeId not in self.follow_dict[followerId]:
            return self.follow_dict[followerId]
        else:
            self.follow_dict[followerId].remove(followeeId)
        



# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)

obj = Twitter()

# // 用户1发送了一条新推文 (用户id = 1, 推文id = 5).
obj.postTweet(1, 4)

# // 用户1的获取推文应当返回一个列表，其中包含一个id为5的推文.
# obj.getNewsFeed(1)

# // 用户1关注了用户2.
# obj.follow(2,1)

# // 用户2发送了一个新推文 (推文id = 6).
# obj.postTweet(2, 5)

# // 用户1的获取推文应当返回一个列表，其中包含两个推文，id分别为 -> [6, 5].
# // 推文id6应当在推文id5之前，因为它是在5之后发送的.
# obj.getNewsFeed(2)

# // 用户1取消关注了用户2.
obj.unfollow(1, 2)

# // 用户1的获取推文应当返回一个列表，其中包含一个id为5的推文.
# // 因为用户1已经不再关注用户2.
obj.getNewsFeed(1)
