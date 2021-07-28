from nltk.stem import WordNetLemmatizer 
from nltk import pos_tag
import numpy as np
import math
from nltk.util import pr
import pandas as pd
import requests
import re
import nltk
from nltk import word_tokenize
from nltk.corpus import stopwords

class TextRank:
    def __init__(self,stl):
        self.stl = stl
        pass

    def word_prepration(self):

        #case folding
        lower_text = self.stl.lower()
        
        #del numbers
        clear_text = re.sub("\d+","", lower_text)

        #tokenize words
        tokenized_words = word_tokenize(clear_text)

        #delete stop words
        stop_words = stopwords.words("english")
        non_stops = []
        for word in tokenized_words:
            if word not in stop_words:
                if word not in non_stops:
                    non_stops.append(word)

        wl = WordNetLemmatizer()
        # tags = {"adj":['JJ','JJR','JJS'], "noun":['NN', 'NNS']}
        taged_text = pos_tag(non_stops)
        lemmatized_words = []

        for word in taged_text:
            w = wl.lemmatize(word[0], pos="a")
            w = wl.lemmatize(w, pos="n")
            w = wl.lemmatize(w, pos="v")
            w = wl.lemmatize(w, pos="r")

            lemmatized_words.append(w)
        
        #create vocab
        vocab = list(set(lemmatized_words))
        return vocab



    def matrix_preration(self):

        vocabulary = self.word_prepration()
        vocab_len = len(vocabulary)

        weighted_edge = np.zeros((vocab_len,vocab_len),dtype=np.float32)

        score = np.zeros((vocab_len),dtype=np.float32)
        window_size = 3
        covered_occurrences = []

        for i in range(0,vocab_len):
            score[i]=1
            for j in range(0,vocab_len):
                if j==i:
                    weighted_edge[i][j]=0
                else:
                    for window_start in range(0,(len(vocabulary)-window_size+1)):
                        
                        window_end = window_start+window_size
                        
                        window = vocabulary[window_start:window_end]
                        
                        if (vocabulary[i] in window) and (vocabulary[j] in window):
                            
                            index_of_i = window_start + window.index(vocabulary[i])
                            index_of_j = window_start + window.index(vocabulary[j])
                            
                            if [index_of_i,index_of_j] not in covered_occurrences:
                                weighted_edge[i][j] += 1
                                covered_occurrences.append([index_of_i,index_of_j])
        return weighted_edge,score,vocabulary



    def score_provider(self):

        weighted_edge,score,vocabulary = self.matrix_preration()
        vocab_len = len(vocabulary)

        inout = np.zeros((vocab_len),dtype=np.float32)

        for i in range(0,vocab_len):
            for j in range(0,vocab_len):
                inout[i]+=weighted_edge[i][j]

        dictionary={}

        MAX_ITERATIONS = 50
        d=0.85
        threshold = 0.0001 #convergence threshold

        for iter in range(0,MAX_ITERATIONS):
            prev_score = np.copy(score)
            
            for i in range(0,vocab_len):
                
                summation = 0
                for j in range(0,vocab_len):
                    if weighted_edge[i][j] != 0:
                        summation += (weighted_edge[i][j]/inout[j])*score[j]
                        
                score[i] = (1-d) + d*(summation)
            
            if np.sum(np.fabs(prev_score-score)) <= threshold: #convergence condition
                print("Converging at iteration "+str(iter)+"....")
                
                score = sorted(score)
                for i in range(0,vocab_len):
                    dictionary[vocabulary[i]] =score[i]
                
                dictionary = {k:v for k,v in sorted(dictionary.items(), key=lambda item: item[1],reverse=True)}
                import itertools
                
                i=0
                for keys,values in dictionary.items():
                    if(i<10):
                        print("Score of "+keys+": "+str(values))
                        i+=1
                break
        return(list(dictionary.keys()))
