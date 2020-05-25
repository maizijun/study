class WordDictionary:
    
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.trie = {}


    def addWord(self, word):
        """
        Adds a word into the data structure.
        """
        tree = self.trie
        for w in word:
            if w not in tree.keys():
                tree[w] = {}

            tree = tree[w]
        tree['end'] = 1

        print(self.trie)


    def search(self, word):
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        """
        #### method 按单词长度为hash值 指在相同长度的单词里找匹配 ####

        def _match(tree,word):
            if len(word)==0:
                return True
            if len(word)==1:
                if list(tree.keys())==['end']:
                    return False
                elif word=='.':
                    return True
                elif word not in tree.keys():
                    return False
                else:
                    return 'end' in tree[word].keys()

            for w in word:
                if w=='.': ## 带点
                    for k in tree.keys():
                        tree = tree[k]
                        word = word[1:]
                        if _match(tree,word):
                            return True
                        else:
                            return False
                
                elif w in tree.keys(): ## 带字符且有子树
                    tree = tree[w]
                    word = word[1:]
                    return _match(tree,word)

                else: ## 没有对应的子树了
                    return False

            if 'end' in tree.keys() == 1:
                return True

        if not self.trie:
            return False

        if list(self.trie.keys())==['end']:
            return False
        else:
            return _match(self.trie,word)




# Your WordDictionary object will be instantiated and called as such:
obj = WordDictionary()
obj.addWord('a')
obj.addWord('ab')

param_2 = obj.search('.a')


print(param_2)