# queue
# stack
# heap 

# Tree
    ## binary search tree 
        假设一个二叉搜索树具有如下特征,
        节点的左子树只包含小于当前节点的数，节点的右子树只包含大于当前节点的数，所有左子树和右子树自身必须也是二叉搜索树

        Q: 如何根据列表构建bst？

    ## trie tree 字典树
        前缀树

        Q：如何根据一堆单词表，构造trie树，并从trie树找到对应单词（或以xxx开头单词，或以.表示任意字符单词）


    ## segment tree 线段树
        线段树是一种非常灵活的数据结构，它可以用于解决多种范围查询问题，比如在对数时间内从数组中找到最小值、最大值、总和、最大公约数、最小公倍数等。线段树既可以用数组也可以用树来实现。对于数组实现，如果索引 i 处的元素不是一个叶节点，那么其左子节点和右子节点分别存储在索引为 2i 和 2i+1 的元素处。

        线段树可以分为以下三个步骤：
        1.从给定数组构建线段树的预处理步骤。
        2.修改元素时更新线段树。
        3.使用线段树进行区域和检索。




# soring

# graph
    ## topological sorting 拓扑排序
        对一个有向无环图(Directed Acyclic Graph简称DAG)G进行拓扑排序，是将G中所有顶点排成一个线性序列，使得图中任意一对顶点u和v，若边<u,v>∈E(G)，则u在线性序列中出现在v之前。通常，这样的线性序列称为满足拓扑次序(Topological Order)的序列,所以严格意义上来说，不是排序算法，且有多种拓扑排序结果

        Q：如何根据依赖关系，构造一个拓扑排序？


    
