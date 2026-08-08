import heapq
from collections import defaultdict

class Twitter:

    def __init__(self):
        self.time = 0
        self.tweetMap = defaultdict(list) # userId -> [(time, tweetId)]
        self.followMap = defaultdict(set) # userId -> set(followeeId)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweetMap[userId].append((self.time, tweetId))
        self.time -= 1

    def getNewsFeed(self, userId: int) -> List[int]:
        res = []
        min_heap = []
        
        relevant_users = self.followMap[userId].copy()
        relevant_users.add(userId)
        
        for user in relevant_users:
            if not self.tweetMap[user]:
                continue

            index = len(self.tweetMap[user]) - 1
            time, tweetId = self.tweetMap[user][index]
            min_heap.append((time, tweetId, user, index - 1))
        
        heapq.heapify(min_heap)

        while min_heap and len(res) < 10:
            time, tweetId, user, index = heapq.heappop(min_heap)
            res.append(tweetId)

            if index >= 0:
                time, tweetId = self.tweetMap[user][index]
                heapq.heappush(min_heap, (time, tweetId, user, index - 1))
        
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId != followeeId:
            self.followMap[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.followMap[followerId].discard(followeeId)
