class Trie:
    ### good question ### 
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.trie = {}


    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        tree = self.trie ## tree 和 self.trie 指向同一个内存地址 ##

        for w in word:
            # print('trie:',self.trie,'tree:',tree)
            if w not in tree.keys():
                tree[w] = {}
            tree = tree[w]

        tree['end']=1

        return self.trie

        
    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        tree = self.trie
        for w in word:
            if w in tree:
                tree = tree[w]
            else:
                return False

        if 'end' in tree.keys():
            return True
        else:
            return False        
        

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        tree = self.trie
        for w in prefix:
            if w in tree:
                tree = tree[w]
            else:
                return False

        return True
        

{'a': {'p': {'p': {'l': {'e': {'end': 1}}}}}, 'p': {'p': {'end': 1}}}

# Your Trie object will be instantiated and called as such:
obj = Trie()
print(obj.insert('apple'))
param_2 = obj.search('app')
param_3 = obj.startsWith('app')
print(obj.insert('app'))
param_4 = obj.search('app')


print(param_2)
print(param_3)
print(param_4)