# 2
import nltk
from nltk.probability import MLEProbDist,FreqDist
from nltk.util import ngrams
from nltk.tokenize import word_tokenize
nltk.download('punkt')
sentence = 'I Love programming in Python and I enjoy learning languages'
tokens = word_tokenize(sentence.lower())
unigram = list(ngrams(tokens,1))
birgram = list(ngrams(tokens,2))
trigram = list(ngrams(tokens,3))

unigram_freq = FreqDist(unigram) 
bigram_freq =  FreqDist(birgram) 
trigram_freq = FreqDist(trigram) 

unigram_prob_dist = MLEProbDist(unigram_freq)
birgram_prob_dist = MLEProbDist(bigram_freq)
trigram_prob_dist = MLEProbDist(trigram_freq)

def get_tok(ngram,prob_dist):
    if not isinstance(ngram,tuple):
        ngram = tuple(ngram)
    return prob_dist.prob(ngram)

print('Unigram : ')
for unigram in unigram_freq: 
    print(f'{unigram[0]} : {get_tok(unigram,unigram_prob_dist)}')
    
print('birgram : ')
for birgram in bigram_freq: 
    print(f'{birgram[0]} : {get_tok(birgram,birgram_prob_dist)}')
    
    
print('trigram : ')
for trigram in trigram_freq: 
    print(f'{trigram[0]} : {get_tok(trigram,trigram_prob_dist)}')
