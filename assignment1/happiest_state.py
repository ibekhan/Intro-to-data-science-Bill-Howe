import sys
import json
from geopy.geocoders import Nominatim
import re

def lines(fp):
    print len(fp.readlines())

def searchDictValue(dictItem, valSearch):
    dictVals = dictItem.values();
    if valSearch in dictVals:
        return dictItem.keys()[dictVals.index(valSearch)]
    else: 
        return None;
                

def main():
    tweet_file = open(sys.argv[1])
    analysis_file = open('analysis-geo.txt','w+')
    #lines(sent_file)
    #lines(tweet_file)

    states = {
        'AK': 'Alaska',
        'AL': 'Alabama',
        'AR': 'Arkansas',
        'AS': 'American Samoa',
        'AZ': 'Arizona',
        'CA': 'California',
        'CO': 'Colorado',
        'CT': 'Connecticut',
        'DC': 'District of Columbia',
        'DE': 'Delaware',
        'FL': 'Florida',
        'GA': 'Georgia',
        'GU': 'Guam',
        'HI': 'Hawaii',
        'IA': 'Iowa',
        'ID': 'Idaho',
        'IL': 'Illinois',
        'IN': 'Indiana',
        'KS': 'Kansas',
        'KY': 'Kentucky',
        'LA': 'Louisiana',
        'MA': 'Massachusetts',
        'MD': 'Maryland',
        'ME': 'Maine',
        'MI': 'Michigan',
        'MN': 'Minnesota',
        'MO': 'Missouri',
        'MP': 'Northern Mariana Islands',
        'MS': 'Mississippi',
        'MT': 'Montana',
        'NA': 'National',
        'NC': 'North Carolina',
        'ND': 'North Dakota',
        'NE': 'Nebraska',
        'NH': 'New Hampshire',
        'NJ': 'New Jersey',
        'NM': 'New Mexico',
        'NV': 'Nevada',
        'NY': 'New York',
        'OH': 'Ohio',
        'OK': 'Oklahoma',
        'OR': 'Oregon',
        'PA': 'Pennsylvania',
        'PR': 'Puerto Rico',
        'RI': 'Rhode Island',
        'SC': 'South Carolina',
        'SD': 'South Dakota',
        'TN': 'Tennessee',
        'TX': 'Texas',
        'UT': 'Utah',
        'VA': 'Virginia',
        'VI': 'Virgin Islands',
        'VT': 'Vermont',
        'WA': 'Washington',
        'WI': 'Wisconsin',
        'WV': 'West Virginia',
        'WY': 'Wyoming'
    }

    stateCount = {}
    geolocator = Nominatim();
    i=0;
    for line in tweet_file:
        i=i+1;
        #if i>6300: break;
            
        print "i = ", i, "len(line) = ", len(line)
        try:
            tweet_converted = json.loads(line);
        except ValueError:
            continue;
        else: 
            tweet_converted = json.loads(line);
        
        coordinates = tweet_converted['coordinates'];
        place = tweet_converted['place'];
        user = tweet_converted['user'];

        if coordinates != None:
            print 'COORDINATE module ', coordinates
            break;
        elif place != None:
            print 'PLACE Module ', place
            if place['full_name'] != None:
                TweetFromState = searchDictValue(states,place['full_name']);
                if TweetFromState in stateCount:
                    stateCount[TweetFromState] += 1;
                else: 
                    stateCount[TweetFromState] = 1;
                print stateCount[TweetFromState]
        else:
            #print 'user', user
            if user['location'] != None:
                #print 'USER Module ', user['location']
                try:
                    location = geolocator.geocode(str(user['location']));
                    addr = location.address
                except:
                    print 'Error in geolocator module'
                    continue;
                
                addr = location.address
                #print 'address raw: ', addr
                addr = re.sub('\d\d\d\d\d,','',addr);
                matchedState1 = re.match('.*,\s*(.*),\s*[Uu]nited',addr); # the first group is junk. the next one should be state
                matchedState2 = re.match('(.*),\s*[Uu]nited',addr); # account for cases when the location is State, United States of America
                if matchedState1 == None:
                    matchedState = matchedState2
                else: matchedState = matchedState1
                #print 'matched state: ', matchedState
                if matchedState != None:
                    print matchedState.group(1)
                    TweetFromState = searchDictValue(states, matchedState.group(1));
                    print TweetFromState
                    if TweetFromState in stateCount:
                        stateCount[TweetFromState] += 1;
                    else: 
                        stateCount[TweetFromState] = 1;
                    print stateCount[TweetFromState]
    
    #print type(tweet_converted)
    #print len(tweet_converted)
    #print sys.getsizeof(tweet_converted)
    
    print stateCount
    
    for key in stateCount:
        #print stateCount[key], key
        analysis_file.write(str(key) +'\t' + str(stateCount[key]) + '\n')

    tweet_file.close()    
    analysis_file.close()

if __name__ == '__main__':
    main()
