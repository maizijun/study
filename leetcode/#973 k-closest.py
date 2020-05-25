class Solution:
    def kClosest(self, points, K):

        # 先计算距离 
        dis = [x**2 + y**2 for x,y in points]
        print(dis)

        # 再进行排序？归并排序？
        def merge(a,b):
            # a,b都是已经排序好序列,讲a,b合并输出c #
            ix,ix1,ix2 = 0,0,0
            l1,l2 = len(a),len(b)

            c = [0 for _ in range(l1+l2)]
            while(ix<l1+l2):
                if ix2==l2 or ix1<l1 and a[ix1]<=b[ix2]:
                    c[ix] = a[ix1]
                    ix1 += 1
                    ix += 1
                elif ix1==l1 or ix2<l2 and a[ix1]>b[ix2]:
                    c[ix] = b[ix2]
                    ix2 += 1
                    ix += 1
                else:
                    break
            return c


        def divide(c):
            n = len(c)

            if n==1:
                return c
            else:
                mid = n//2
                a,b = c[:mid],c[mid:]
                a = divide(a)
                b = divide(b)

            return merge(a,b)

        res = divide(dis)
        res = res[:K]
        print(res)
        return [[x,y] for x,y in points if x**2+y**2 in res]

a = Solution()
print(a.kClosest([[3,3],[5,-1],[-2,4]],2))


