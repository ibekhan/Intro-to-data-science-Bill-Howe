import sys
import json

def lines(fp):
    print len(fp.readlines())

def main():
    word_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    analysis_file = open('analysis.txt','w+')
    #lines(sent_file)
    #lines(tweet_file)

    word_dict = {} # initialize an empty dictionary
    for line in word_file:
        term, score  = line.split("\t")  # The file is tab-delimited. "\t" means "tab character"
        word_dict[term] = int(score);  # Convert the score to an integer.
    word_file.close()
    #print word_dict.items() # Print every (term, score) pair in the dictionary
    i=0;
    for line in tweet_file:
        i=i+1
        print 'i=', i, len(line)
            
        try:
            tweet_converted = json.loads(line);
        except ValueError:
            continue;
        else: 
            tweet_converted = json.loads(line);
        
        tweet_text = tweet_converted['text'];
        print tweet_text
        words = tweet_text.split();
        sentiment = 0;
        for word in words:
            word_edited = filter(lambda w: w.isalpha(),word); # to remove any special characters from words
            # word_edited = ''.join(w for w in word if w.isalpha()); # another way of doing same 
            print word, word_edited
            if word_edited in word_dict:
                sentiment = sentiment + word_dict[word_edited]
                print word, word_edited, sentiment
            
        print "total=", sentiment
        analysis_file.write(str(sentiment)+'\n');
        analysis_file.write(str(words)+'\n');
        
    
    #print type(tweet_converted)
    #print len(tweet_converted)
    #print sys.getsizeof(tweet_converted)
    
    tweet_file.close()    
    analysis_file.close()

if __name__ == '__main__':
    main()
