class Solution:
    def lemonadeChange(self, bills) -> bool:

        is_fiv = 0
        is_ten = 0

        for bill in bills:
            if bill==5:
                is_fiv+=1

            if bill==10:
                if is_fiv<=0:
                    return False
                else:
                    is_ten+=1
                    is_fiv-=1

            if bill==20:
                if is_fiv<=0:
                    return False
                elif is_ten>0:
                    is_ten-=1
                    is_fiv-=1
                elif is_fiv<=2:
                    return False
                else:
                    is_fiv-=3

        return True

a = Solution()
print(a.lemonadeChange([10,10,10,10,20]))
