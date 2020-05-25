class Solution:
    def sortString(self, s):

        count_dict = {k:s.count(k) for k in set(s)}
        count_dict = {k:count_dict[k] for k in sorted(count_dict.keys())}

        res = []

        # print(count_dict)

        # print(count_dict.keys())
        while(count_dict):

            for k in list(count_dict.keys())[:]:
                count_dict[k] -= 1
                res.append(k)
                print(k)

                if count_dict[k]==0:
                    del count_dict[k]

            for k in list(count_dict.keys())[::-1]:
                count_dict[k] -= 1
                res.append(k)
                print(k)

                if count_dict[k]==0:
                    del count_dict[k]

        return ''.join(res)



a = Solution()
print(a.sortString('leetcode'))