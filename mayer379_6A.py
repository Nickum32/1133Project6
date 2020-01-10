# CSci 1133 HW 6
# Nicholas Mayer
# HW Problem A
#
# Compares two dictionaries and returns a dictionary with keys that were shared
# between the original two dictionaries

def compareDicts(d1, d2):
    lowerd1 = {} # create a new dictionary for the lower case keys of d1 and d2
    lowerd2 = {}
    dSame = {}
    for item in d1.keys(): # converts all keys to lowercase
        lowerd1[item.lower()] = d1[item]
    for item in d2.keys(): # converts all keys to lowercase
        lowerd2[item.lower()] = d2[item]
    for key in lowerd1.keys(): # iterates for every key in lowerd1
        if key in lowerd2.keys(): # checks if key is in lowerd2
            dSame[key] = lowerd2[key] + lowerd1[key] # adds key and the sum of corresponding values
    return dSame  
