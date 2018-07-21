############################PACKAGES
import pandas as pd
import numpy as np
from scipy import spatial
from gensim.models.doc2vec import  Doc2Vec
import nltk
from nltk.corpus import stopwords
import os
from  dateutil import parser
import re
#os.chdir("doc2vecmodel")  ######### CHANGE THE PATH AS PER YOUR LOCATION
##############################################################################################

################ READ THE CSV FILE################################################################
df=0
df=pd.read_csv("preprocessed.csv")
df['questions'].fillna("nothing",inplace=True)   ###  filling empty  values  with  'nothing' if present

##################################################################################################

################### INSIDE THIS CLASS , THERE  ARE 3 FUNCTIONS  :
                   # 1 .avg_feature_vector functon :  average vector for all words in every sentence .
                   # 2. cosine_dist  function       : finding cosine similarity between average of vectors .
                   # 3. preprocedd_user_inpt        : Preprocess the user input before passing it to function .

class one():

    ######################### THIS FUNCTION WILL  CREATE  FEATURE VECTORS  FOR EVERY TOKENS
    def avg_feature_vector(sentence, model, num_features, index2word_set):
        words = sentence.split()
        feature_vec = np.zeros((num_features,), dtype='float32')
        n_words = 0
        for word in words:
            if word in index2word_set:
                n_words += 1
                feature_vec = np.add(feature_vec, model[word])
        if (n_words > 0):
            feature_vec = np.divide(feature_vec, n_words)
        return feature_vec

    ################################################################################################

    ####  COSINE SIMILARITY BETWEEN  SENTENCES ######################################################

    def cosine_dist(user_asked,df):
        model_new = Doc2Vec.load("doc2vec2.model")  ####  import  doc2model
        index2word_set = set(model_new.wv.index2word)
        try:
            all_ratios=[]
            questn_df=pd.DataFrame({})
            for i in range(df.__len__()):
                s1_afv = one.avg_feature_vector(user_asked, model=model_new, num_features=100, index2word_set=index2word_set)
                s2_afv = one.avg_feature_vector(df['questions'][i], model=model_new, num_features=100, index2word_set=index2word_set)
                all_ratios.append(1 - spatial.distance.cosine(s1_afv, s2_afv))
            questn_df= pd.DataFrame({"questions":list(df['questions']),"answers":list(df['answers']), "type":list(df['type']),
                                     "ratios":all_ratios})
            final_ratio = questn_df.sort_values('ratios', ascending=False)
            #final_ratio_top_80_percent=final_ratio[(final_ratio.ratios>=0.65)]

            if final_ratio.empty:

                return 'sorry  didnt  understand  your question'
            else:

                return final_ratio.head(5)
        except:
             return 'sorry  didnt  understand  your question'

    ###############################################################################################################################

    #################PREPROCESS  THE USER INPUT  BEFORE  PASSING IT TO FUNCTION ####################################################

    def  preprocedd_user_inpt(user_asked):
        a=user_asked.lower()
        stop_words = set(stopwords.words('english'))
        preprocess = []
        from nltk.tokenize import TweetTokenizer
        tknzr = TweetTokenizer()
        preprocess.append(tknzr.tokenize(a)) ### tokenize  user input
        filtered_sentence = " ".join([w for w in preprocess[0] if not w in stop_words]) ##  remove stopwords
        words = filtered_sentence###  remove punchuation
        return words

##############################################################################################################################


    ####  CODES  TO PREDICT  THE ANSWERS #########################################################################################

################################## THIS MAIN  FUNCTION IS TO  TAKE INPUT FROM USERS AND CALL  THE ABOVE CLASS FUNCTIONS .

def  Main_function():
    print('write your question below : ')  #### initial  message  shown to users
    user_ask =input()
    ############### asking  for user input from the user in below
    user_inpt=int(input('Press 1 to know the answer to your question  | Press 2 to know top 5 probabable  matching answers'))

    if(user_inpt==1):
        userIp=one.preprocedd_user_inpt(user_ask)   ######## Calling the  preprocesser  function from class 'one'
        predict_question=one.cosine_dist(user_ask,df).iloc[0].answers  #### Calling the cosine_dist function from class 'one'
        print(predict_question)
        return predict_question
    elif(user_inpt==2):
        userIp = one.preprocedd_user_inpt(user_ask) ######## Calling the  preprocesser  function from class 'one'
        predict_question = one.cosine_dist(user_ask, df)[['questions','answers','ratios']] #### Calling the cosine_dist function from class 'one'
        print(predict_question)
        return predict_question
    else:
        print('please type 1 or 2 for answer')


##################################CALLING THE  MAIN FUNCTION TO EXECUTE ############################

if __name__=='__main__':
    Main_function()

######################################################################################################

