class Solution:
    def simplifyPath(self, path):

        if not path:
            return '/'
        if path == '/':
            return '/'

        path_all = []

        for p in path.split('/'):
            if p=='/':
                continue
            elif p=='':
                continue
            elif p=='.':
                continue

            elif p=='..':
                if path_all:
                    path_all.pop()
                
                # while path_all and path_all[-1]!='/':
                #     path_all.pop()
                
                # if path_all:
                #     path_all.pop() ## 删掉'/'

                # continue
            
            else:
                # path_all.append('/')
                path_all.append(p)

        print(path_all)
        
        return '/'+'/'.join(path_all) if len(path_all)!=0 else '/'

a = Solution()
print(a.simplifyPath("/a//b////c/d//././/.."))
# print(a.simplifyPath("/../"))





            

