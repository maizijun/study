class Solution:
    def canFinish(self, numCourses, prerequisites):

        #### dfs ####

        visit = [0 for _ in range(numCourses)]
        adja = [[] for _ in range(numCourses)]

        for cur,pre in prerequisites:
            adja[pre].append(cur)

        print(adja)


        def helperr(i):
            '''
            判断第i个节点是否遍历完成，且无环
            0表示没遍历
            1表示正在遍历中
            2表示遍历完成
            '''

            if visit[i]==1: ##表示遍历中又回到了原点，表示环
                return False
            if visit[i]==2: ##表示遍历完成，直接退出
                return True

            visit[i]=1
            for x in adja[i]:
                if not helperr(x):
                    return False
            visit[i]=2

            return True

        for x in range(numCourses):
            if not helperr(x):
                return False
        
        return True
            
a = Solution()
print(a.canFinish(2,[[1,0]]))