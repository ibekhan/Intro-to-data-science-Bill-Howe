import MapReduce
import sys
import json

mr = MapReduce.MapReduce();

def mapper(record): # takes a text, list etc input and returns a key-value pair
    # The MapReduce class breaks up a json file and 
    # passes on the text input to mapper function
    key = record[0];
    value = record[1];
    words = value.split();
    for w in words:
        mr.emit_intermediate(w,key);
    
def reducer(key, list_of_values): # takes a key and list input
    # returns a value output for that key from that list
    total = list(set(list_of_values))
    print key, total
    #mr.emit(key, total)
    
def main():
    bookfile = open(sys.argv[1]);
    mr.execute(bookfile, mapper, reducer);
    
if __name__ == '__main__':
    main()
