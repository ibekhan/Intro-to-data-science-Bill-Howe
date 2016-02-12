import MapReduce
import sys
import json

mr = MapReduce.MapReduce();

def mapper(record): # takes a text, list etc input and returns a key-value pair
    # The MapReduce class breaks up a json file and 
    # passes on the text input to mapper function
    key = int(record[1]); #make orderID in each line as the key
    value = record;
    mr.emit_intermediate(key,value);
    
def reducer(key, list_of_values): # takes a key and list input
    # returns a value output for that key from that list
    # mr.emit(key, total)
    print key
    print list_of_values
    print len(list_of_values)
    joined = [];
    for items1 in list_of_values:
        for items2 in list_of_values:
            if items1[0] == "order" and items2[0] == "line_item":
                joined.append(items1 + items2)
    print "print joined\n"
    print joined;
    print len(joined)
    mr.emit(joined)

def main():
    joinfile = open(sys.argv[1]);
    mr.execute(joinfile, mapper, reducer);
    
if __name__ == '__main__':
    main()
