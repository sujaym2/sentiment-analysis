class Vectorizer(): 
    countVectorizer = CountVectorizer(analyzer=clean_text) 
    countVector = countVectorizer.fit_transform(tw_list[‘text’])
    print(‘{} Number of reviews has {} words’.format(countVector.shape[0], countVector.shape[1]))
   
    count_vect_df.head()

    def get_top_n_gram(corpus,ngram_range,n=None):
 vec = CountVectorizer(ngram_range=ngram_range,stop_words = ‘english’).fit(corpus)
 bag_of_words = vec.transform(corpus)
 sum_words = bag_of_words.sum(axis=0) 
 words_freq = [(word, sum_words[0, idx]) for word, idx in vec.vocabulary_.items()]
 words_freq =sorted(words_freq, key = lambda x: x[1], reverse=True)
 return words_freq[:n]#n2_bigram
n2_bigrams = get_top_n_gram(tw_list[‘text’],(2,2),20)n2_bigrams
