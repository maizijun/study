'''
Given two strings s1 and s2, write a function to return true if s2 contains the permutation of s1.
In other words, one of the first string's permutations is the substring of the second string.
Example 1:
Input: s1 = "ab" s2 = "eidbaooo"
Output: True
Explanation: s2 contains one permutation of s1 ("ba").
Example 2:
Input:s1= "ab" s2 = "eidboaoo"
Output: False
Note:
The input strings only contain lower case letters.
The length of both given strings is in range [1, 10,000].
'''
'''
题目理解;
给定两个字符串 s1 和 s2，写一个函数来判断 s2 是否包含 s1 的排列。
换句话说，第一个字符串的排列之一是第二个字符串的子串。
示例1:
输入: s1 = "ab" s2 = "eidbaooo"
输出: True
解释: s2 包含 s1 的排列之一 ("ba").
示例2:
输入: s1= "ab" s2 = "eidboaoo"
输出: False
注意：
输入的字符串只包含小写字母
两个字符串的长度都在 [1, 10,000] 之间

思考过程：
遇到问题先想暴力法，问题是s1的排列是不是s2的子串。
方法一 暴力法 [超过时间限制]
最简单的方法是生成短字符串s1的所有排列，并检查生成的排列是否是s2字符串的子字符串。
（生成所有可能的配对，可以采用交换位置法）

方法二 排序 [超过时间限制]
如何优化上诉暴力法呢？那就是采用排序统计全部字符出现次数，简化问题，如下：
只有当两个字符串包含相同次数的相同字符时，一个字符串才是另一个字符串的排列。
即sorted(x)= sorted(y)时，一个字符串x才​​是字符串 y 的排列。
为了检查这一点，我们可以用循环以一定滑动窗口在s2上面进行遍历，并比较sorted(x)= sorted(y)
显然这种算法是无法满足时间复杂度要求的，因为每个窗口都要sort一遍，sort最快也要o（n）

方法三 使用单纯哈希表 [通过]
方法二中sort排序太耗时，其实排列是一种排列组合，不包含顺序，那很自然可以用哈希表统计。
只有当两个字符串包含具有相同频率的相同字符时，一个字符串才是另一个字符串的排列，其实就是省略了方法二中的有序性的时间。
可以采用循环以一定滑动窗口在s2上面进行遍历，并检查出现在s1和s2中的字符出现的频率。如果每个字母的频率完全匹配，
则只有 s1 的排列可以是 s2 的子字符串。
显然这种算法虽然省略了有序性，但是构造哈希表也比较耗时

方法四 使用数组（字符哈希） [通过，用c++比较好实现]
方法三的哈希表构造比较耗时，题目中只有小写字母，因此很自然可以想到字符哈希，他是一种数组形式。
普及字符哈希：
因为小写字母对应ASCII码，因此字典一般是这样{字母-频率}{a：2}，由于ASCII码，可以变为{a的ASCII码：2}，此时的key就变味了数字，
所以就有了字符哈希，采用数组的形式，数组下标就是对应的key，也就是字母，数组的值就是对应的value，也就是该字母出现的频率。
可以使用更简单的数组数据结构来存储频率，而不是仅使用特殊的哈希表数据结构来存储字符出现的频率。
给定字符串仅包含小写字母（'a'到'z'）。因此我们需要采用大小为 26 的数组。其余过程与最后一种方法保持一致。

方法五 滑动窗口（更新边界法） [通过，在方法四基础上进行实现更快，也可以在方法三上实现加速]:
可以为 s2中的第一个窗口创建一次哈希表，而不是为 s2中考虑的每个窗口重新生成哈希表。
此时，滑动窗口每次滑动，其实只改变了边界情况，即删除了一个最前面的字符，加入了一个最后面的字符。

方法六 优化的滑动窗口（变量统计法） [通过]:
如果面试官还让你优化，那么就考虑哪些信息是无用，保留更少的信息，时间复杂度就越低，
显然并不用保存一个哈希表，哪怕只是更新边界都没有必要，只需要统计26个小写字母，哪些符合要求即可，如下；
不是比较每个更新的 s2map 的哈希表的所有元素，而是对应于 s2考虑的每个窗口，
我们会跟踪先前哈希表中已经匹配的元素数量当我们向右移动窗口时，只更新匹配元素的数量。
（这里就是26个字母出现的次数，比如s1有ab，那么对于s2滑动窗口，保证ab次数出现为1，其余为0，用一个cnt变量记录即可）
为此，我们维护一个 count变量，该变量存储字符数（s1出现的全部字母），这些字符在 s1中具有相同的出现频率，
当前窗口在 s2中。当我们滑动窗口时，如果扣除第一个元素并添加新元素导致任何字符的新频率匹配，我们将 count递增1.
如果不是，我们保持 count 不变或者-1。如果在移动窗口后，count的计算结果为26，则表示所有字符的频率完全匹配，返回True。
-------------------------------------华丽的分割线---------------------------------------
至此，你已经掌握了本题的求解思想，此时回头看答案就很easy
对于答案代码：
方法1：其实就是滑动窗口哈希表（更新边界法），对应上面的方法五
class Solution(object):
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        l1, l2 = len(s1), len(s2)
        c1 = collections.Counter(s1) #s1的哈希表，实质是字典
        c2 = collections.Counter() #实例化一个counter类
        p = q = 0  #设定下标初始化为0，滑动窗口就是[p,q]
        #下面就是不断在s2上面进行滑动窗口，不断更新哈希表进行比较，这是采用的边界更新法哦，因此是方法五，而不是方法三
        #这里补充一下，为什么滑动窗口用while没用for，其实都是一样的，你也可以改成for
        #但是对于有些情况，就只能用while，比如在回溯算法里面，即循环变量需要频繁的加减，显然此题并不是
        #因此对于此题，用for也可以，整体来说while的应用场合更加广泛
        while q < l2:
            c2[s2[q]] += 1   #统计字典哈希表
            if c1 == c2:
                return True  #注意，这种结果性条件判断一定是写在前面
            q += 1           #s2滑动窗口，下标后移
            if q - p + 1 > l1:   #为什么有这个呢？因为第一个滑动窗口比较特殊，要先构造第一个完整的滑动窗口，后面才是更新边界
                c2[s2[p]] -= 1   #字典哈希表移除最前面的字符
                if c2[s2[p]] == 0:  #由于counter特性，如果value为0，就删除它
                #否则会出现s1的map没有a，但是s2的map的a为0，此时是成立的，但是导致了这两个map不相等，结果出错
                    del c2[s2[p]]
                p += 1     #最前面的下标右移动
        return False  #遍历所有滑动窗口过后，仍然没返回true，那就是不合题意
        
方法2：优化的滑动窗口（变量统计法），其实就是上面的方法六
class Solution(object):
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        l1, l2 = len(s1), len(s2)
        c1 = collections.Counter(s1)
        c2 = collections.Counter()
        cnt = 0 #统计变量，全部26个字符，频率相同的个数，当cnt==s1字母的个数的时候，就是全部符合题意，返回真
        p = q = 0 #滑动窗口[p,q]
        while q < l2:
            c2[s2[q]] += 1
            if c1[s2[q]] == c2[s2[q]]: #对于遍历到的字母，如果出现次数相同
                cnt += 1               #统计变量+1
            if cnt == len(c1):         #判断结果写在前面，此时证明s2滑动窗口和s1全部字符相同，返回真
                return True
            q += 1                     #滑动窗口右移
            if q - p + 1 > l1:         #这是构造第一个滑动窗口的特殊判断，里面内容是维护边界滑动窗口
                if c1[s2[p]] == c2[s2[p]]:    #判断性的if写在前面，因为一旦频率变化，这个统计变量就减1
                    cnt -= 1
                c2[s2[p]] -= 1                #字典哈希表移除最前面的字符
                if c2[s2[p]] == 0:            #由于counter特性，如果value为0，必须删除它
                    del c2[s2[p]]
                p += 1                        #最前面的下标右移动
        return False
'''


class Solution(object):
    ## good question ## hash method 
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        n1,n2 = len(s1),len(s2)
        
        import collections
        coll1 = collections.Counter(s1)
        coll2 = collections.Counter()

        # q = 0
        for q in range(len(s2)):
            # print(coll1)
            # print(q,coll2)
            
            if q<n1-1:
                coll2[s2[q]]+=1
                # q += 1
                continue
            else:
                coll2[s2[q]] += 1
                if q>=n1:
                    coll2[s2[q-n1]] -= 1                
                    if coll2[s2[q-n1]]==0:
                        del coll2[s2[q-n1]]
            if coll1 == coll2:
                return True

            print(coll2)

                # q += 1
        return False
        



a = Solution()
print(a.checkInclusion(s1 = "a", s2 = "ab"))

