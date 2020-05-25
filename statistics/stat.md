# Sampling 
    ## Reject Sampling 
    ## Maetropolitan Sampling
    ## Reservoir Sampling
        给定一个数据流，数据流长度N很大，且N直到处理完所有数据之前都不可知，请问如何在只遍历一遍数据（O(N)）的情况下，能够随机选取出m个数据。

        1.数据流长度N很大且不可知，所以不能一次性存入内存。
        2.时间复杂度为O(N)。
        3.随机选取m个数，每个数被选中的概率为m/N

        算法思路大致如下：
        1.如果接收的数据量小于m，则依次放入蓄水池。
        2.当接收到第i个数据时，i >= m，在[0, i]范围内取以随机数d，若d的落在[0, m-1]范围内，则3.用接收到的第i个数据替换蓄水池中的第d个数据。
        4.重复步骤2。






# Regression
    ## SVM
    ## (Generalize) Linear Regression
    ## Gaussian Process


# Classification

# Tree

# Nonparametric estimation

# Time Series


