import pandas as pd
import numpy as np
from scipy import spatial
from gensim.models.doc2vec import  Doc2Vec
from nltk.corpus import stopwords
from nltk.tokenize import TweetTokenizer

class QABot:

    def __init__(self,data,model):
        self.df = data
        self.model = model

    def avg_feature_vector(self,sentence, model, num_features, index2word_set):
        """
        creting vectors for each tokens
        Explain more.
        :param sentence:
        :param model:
        :param num_features:
        :param index2word_set:
        :return:
        """
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

    def cosine_dist(self, user_asked):
        """
        coisine similarity between sentences
        Explain more.
        :param user_asked:
        :param df:
        :return:
        """

        #model_new = Doc2Vec.load("doc2vec2.model")  ####  import  doc2model
        index2word_set = set(self.model.wv.index2word)
        try:
            all_ratios=[]
            questn_df=pd.DataFrame({})
            for i in range(self.df.__len__()):
                s1_afv = self.avg_feature_vector(user_asked, model=self.model, num_features=100, index2word_set=index2word_set)
                s2_afv = self.avg_feature_vector(self.df['questions'][i], model=self.model, num_features=100, index2word_set=index2word_set)
                all_ratios.append(1 - spatial.distance.cosine(s1_afv, s2_afv))
            questn_df= pd.DataFrame({"questions":list(self.df['questions']),"answers":list(self.df['answers']), "type":list(self.df['type']),
                                     "ratios":all_ratios})
            final_ratio = questn_df.sort_values('ratios', ascending=False)
            #final_ratio_top_80_percent=final_ratio[(final_ratio.ratios>=0.65)]

            if final_ratio.empty:

                return 'sorry  didnt  understand  your question'
            else:

                return final_ratio.head(5)
        except:
             return 'sorry  didnt  understand  your question'

    def preprocedd_user_inpt(self,user_asked):
        """
        Explain the module
        :param user_asked:
        :return:
        """
        a = user_asked.lower()
        stop_words = set(stopwords.words('english'))
        preprocess = []
        tknzr = TweetTokenizer()
        preprocess.append(tknzr.tokenize(a))  ### tokenize  user input
        filtered_sentence = " ".join([w for w in preprocess[0] if not w in stop_words])  ##  remove stopwords
        words = filtered_sentence  ###  remove punchuation
        return words

def main():
    # os.chdir("doc2vecmodel")
    data = pd.read_csv("preprocessed.csv")
    model = Doc2Vec.load("doc2vec2.model")  ####  import  doc2model
    data['questions'].fillna("nothing", inplace=True)  ###  filling empty  values  with  'nothing' if present

    Bot = QABot(data, model)

    print('write your question below : ')  #### initial  message  shown to users
    user_ask = input()
    ############### asking  for user input from the user in below
    user_inpt = int(
        input('Press 1 to know the answer to your question  | Press 2 to know top 5 probabable  matching answers'))

    if (user_inpt == 1):
        userIp = Bot.preprocedd_user_inpt(user_ask)  ######## Calling the  preprocesser  function from class 'one'
        predict_question = Bot.cosine_dist(user_ask).iloc[
            0].answers  #### Calling the cosine_dist function from class 'one'
        print(predict_question)
    elif (user_inpt == 2):
        userIp = Bot.preprocedd_user_inpt(user_ask)  ######## Calling the  preprocesser  function from class 'one'
        predict_question = Bot.cosine_dist(user_ask)[
            ['questions', 'answers', 'ratios']]  #### Calling the cosine_dist function from class 'one'
        print(predict_question)

    else:
        print('please type 1 or 2 for answer')


if __name__=='__main__':
    main()