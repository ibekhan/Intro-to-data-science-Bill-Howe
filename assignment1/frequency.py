import sys
import json
import collections
import re

def main():
    tweet_file = open(sys.argv[1])
    analysis_file = open('analysis-freq.txt','w+')

    i=0;
    word_dict = collections.OrderedDict() # initialize an empty ordered dictionary
    for line in tweet_file:
        i=i+1;
        print "i = ", i, "len(line) = ", len(line)
        #if i>10: break;
        try:
            tweet_converted = json.loads(line);
        except:
            continue;
        
        tweet_text = tweet_converted['text'];
        tweet_text = re.sub('http\S*','',tweet_text)
        words = tweet_text.split();
        for word in words:
            word_edited = filter(lambda w: w.isalpha(),word); # to remove any special characters from words
            # word_edited = ''.join(w for w in word if w.isalpha()); # another way of doing same 
            word_edited = word_edited.lower();
            word_dict[word_edited] = word_dict.get(word_edited,0)+1
            word_dict = collections.OrderedDict(sorted(word_dict.items()));
    
    print len(word_dict)
    
    word_dict = collections.OrderedDict(sorted(word_dict.items(),key=lambda t:t[1],reverse=True))
    print word_dict
    for key in word_dict:
        analysis_file.write(str(key) +'\t' + str(word_dict[key]) + '\n')

    
    tweet_file.close()    
    analysis_file.close()

if __name__ == '__main__':
    main()
