import MapReduce
import sys
import json

mr = MapReduce.MapReduce();

def mapper(record): # takes a text, list etc input and returns a key-value pair
    # The MapReduce class breaks up a json file and 
    # passes on the text input to mapper function
    key = record[0]; #make orderID in each line as the key
    value = record[1][:-10];
    mr.emit_intermediate('trimmed',value);
    
def reducer(key, list_of_values): # takes a key and list input
    # returns a value output for that key from that list
    nodup = list(set(list_of_values))
    print len(nodup)
    mr.emit(nodup)

def main():
    dnafile = open(sys.argv[1]);
    mr.execute(dnafile, mapper, reducer);
    
if __name__ == '__main__':
    main()
