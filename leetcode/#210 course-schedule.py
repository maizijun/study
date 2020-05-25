class Solution:
    def findOrder(self, numCourses, prerequisites):

        res = []
        
        #### BFS ####
        ## 建立adjacent矩阵 ##
        adjn = [[] for _ in range(numCourses)]
        in_degree = {k:0 for k in range(numCourses)}  ## 记录入度 与 出度
        out_degree = {k:0 for k in range(numCourses)}

        for post,pre in prerequisites:
            adjn[pre].append(post)
            in_degree[post] = in_degree.get(post,0)+1
            out_degree[pre] = out_degree.get(pre,0)+1

        is0 = [k for k in in_degree if in_degree[k]==0]

        if len(is0)==0:
            return []

        print(adjn)
        res += is0
        # print(res)
        
        for course in res:
            neigbors = adjn[course]
            for n in neigbors:
                in_degree[n] -= 1

                if in_degree[n]==0:
                    res.append(n)
                    print(res)

            adjn[course] = []

        if len(res) != numCourses:
            return []
        else:
            return res

        # print(res)
        # print(in_degree,out_degree)


a = Solution()
print(a.findOrder(3,[[1,0],[1,2]]))