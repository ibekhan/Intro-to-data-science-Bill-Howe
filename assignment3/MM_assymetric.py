import MapReduce
import sys
import json

mr = MapReduce.MapReduce();

def mapper(record): # takes a text, list etc input and returns a key-value pair
    # The MapReduce class breaks up a json file and 
    # passes on the text input to mapper function
    key = record[0]; #make orderID in each line as the key
    value = record[1];
    mr.emit_intermediate(key,value);
    
def reducer(key, list_of_values): # takes a key and list input
    # returns a value output for that key from that list
    assymetric = [];
    for item in list_of_values:
        if item not in mr.intermediate:
            assymetric.append([key, item])
        else:
            if not (key in mr.intermediate[item]):
                assymetric.append([key, item])
    print key, "\n", assymetric, "\n", len(assymetric)
    mr.emit(assymetric)

def main():
    friendfile = open(sys.argv[1]);
    mr.execute(friendfile, mapper, reducer);
    
if __name__ == '__main__':
    main()
