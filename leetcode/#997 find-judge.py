class Solution:
    def findJudge(self, N, trust):

        if len(trust)==1:
            return trust

        from collections import defaultdict
        conn = defaultdict(list)
        conn2 = defaultdict(list)

        all_trust = []

        for a,b in trust:
            conn[b].append(a)
            if len(conn[b])==N-1:
                all_trust.append(b)

        for a,b in trust:
            conn2[a].append(b)

        for bb in all_trust:
            if bb not in conn2.keys():
                return bb
            
        return -1


a = Solution()
print(a.findJudge(4,[[1,3],[2,3],[3,1]]))
