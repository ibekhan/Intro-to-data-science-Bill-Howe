import sys
import json

def main():
    word_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    analysis_file = open('analysis-term.txt','w+')

    word_dict = {} # initialize an empty dictionary
    for line in word_file:
        term, score  = line.split("\t")  # The file is tab-delimited. "\t" means "tab character"
        word_dict[term] = int(score);  # Convert the score to an integer.
    word_file.close()

    i=0;
    for line in tweet_file:
        i=i+1
        print 'i=', i, len(line)
            
        try:
            tweet_converted = json.loads(line);
        except:
            continue;
        
        tweet_text = tweet_converted['text'];
        words = tweet_text.split();
        sentiment = 0;
        for word in words:
            word_edited = filter(lambda w: w.isalpha(),word); # to remove any special characters from words
            # word_edited = ''.join(w for w in word if w.isalpha()); # another way of doing same 
            sentiment = sentiment + word_dict.get(word_edited,0)

        print "total=", sentiment
        analysis_file.write(str(words)+'\n'+str(sentiment)+'\n');
            
    tweet_file.close()    
    analysis_file.close()

if __name__ == '__main__':
    main()
