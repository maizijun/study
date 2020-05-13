
from gensim.test.utils import common_texts,get_tmpfile
from gensim.models import word2vec
from gensim import corpora


from nltk.corpus import reuters,stopwords
from nltk.tokenize import sent_tokenize,word_tokenize,RegexpTokenizer

from nltk import Text

import numpy as np
import pandas as pd
import re,string

# from pprint import pprint


def gen_text(text_nums=100):
    '''        
    generate text from corpus
    
    input: corpus ID
    return: list, each for one text
    '''

    corp_select = reuters
    id_ls =  corp_select.fileids()

    text_ls = []
    for k in range(text_nums):
        text_ls.append(corp_select.raw(fileids=id_ls[k]))

    return text_ls


def gen_sentence(text_ls):
    '''
    generate tokenized sentences from text list
    
    input: corpus ID
    return: list, each for one sentence
    '''

    sen_ls = []
    for text in text_ls:
        sen_ls = sen_ls + sent_tokenize(text)

    return sen_ls


def remove_punc(word):
    ''' 去除标点符号 remove punctuation from word'''

    trans=str.maketrans({key: None for key in string.punctuation}) #建立转换关系
    word = word.translate(trans)

    return word


def gen_word(sentence):
    '''
    generate tokenized words from sentence
    remove punctuation

    input: sentence
    return: list, each element for one word
    '''

    word_ls = []
    reg_tokenizer_b = RegexpTokenizer(r'\s+',gaps=True) ## 按照空格划分
    reg_tokenizer_w = RegexpTokenizer(r'\w+') ## 按照单词

    
        # word_ls.append(word_tokenize(sen))

    word_ls = reg_tokenizer_b.tokenize(sentence)
    # word_ls = list(filter(lambda x:x not in stopwords.words('english'),word_ls))
    # word_ls = list(filter(lambda x:x not in [*map(lambda x:x.upper(),stopwords.words('english'))],word_ls))

    word_ls = list(map(lambda x:re.sub("[0-9]+","",x),word_ls))
    word_ls = list(map(lambda x:x.lower(),word_ls))
        # word_ls_tmp = list(map(lambda x:x.translate(trans),word_ls_tmp))

    word_ls = list(map(remove_punc,word_ls))
    word_ls = list(filter(lambda x:len(x)>0,word_ls)) ## 去掉空格 

    return word_ls




if __name__ == '__main__':

    text_ls = gen_text()
    sen_ls = gen_sentence(text_ls)

    print(len(text_ls),len(sen_ls))

    word_sen_ls = []
    word_ls = []

    for xx in sen_ls:
        word_sen_ls.append(gen_word(xx))
        word_ls = word_ls + gen_word(xx)


    vocab = np.unique(word_ls)
    print(len(text_ls),len(word_sen_ls),len(word_ls),len(vocab))

    word_ls = pd.Series(word_ls)
    is_common_word = word_ls.value_counts()>=50
    vocab = is_common_word[is_common_word==True].index.tolist()
    print(len(vocab))


    wv_model = word2vec.Word2Vec(word_sen_ls,size=100,window=5)
    model_vocab = list(wv_model.wv.vocab.keys())

    df_word_vec = pd.DataFrame(index=vocab,columns=['vec_'+str(i) for i in range(100)])

    for i,word in enumerate(df_word_vec.index[:]):
        # if i%100==0:
        #     print(i)
        df_word_vec.loc[word] = wv_model.wv.word_vec(word).round(4)


    df_word_vec.head()
