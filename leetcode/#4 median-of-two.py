class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        
        def find_k(nums1,nums2,k): ## 使用二分法找到第k个数 ##
            ix1,ix2 = 0,0

            n1,n2 = len(nums1),len(nums2)

            while k>0:
                print(ix1,ix2)
                mid = k//2-1
                # print(k,mid)

                if ix1==n1:
                    return nums2[ix2+mid+1]
                if ix2==n2:
                    return nums1[ix1+mid+1]
                if k==1:
                    return min(nums1[0],nums2[0])
                
                newix1 = min(ix1+mid,n1-1)
                newix2 = min(ix2+mid,n2-1)

                var1 = nums1[newix1]
                var2 = nums2[newix2]

                if var1<=var2:
                    k -= newix1-ix1+1
                    ix1 = newix1 + 1
                else:
                    k -= newix2-ix2+1
                    ix2 = newix2 + 1


        n1,n2 = len(nums1),len(nums2)
        n = n1 + n2

        if n%2==1:
            return find_k(nums1,nums2,n//2+1)
        else:
            return (find_k(nums1,nums2,n//2+1)+find_k(nums1,nums2,n//2))/2


a = Solution()
print(a.findMedianSortedArrays([1,2],[3,4]))



