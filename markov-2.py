import sys
import random


def make_chains(corpus):
    """Takes input text as string; returns dictionary of markov chains."""
    text_file = open(corpus)
    full_text_string = []
    for line in text_file:
        text_list = line.rstrip().split()
        full_text_string.extend(text_list)
    
    #print full_text_string
    
    length_full_text = len(full_text_string)-2
    ngrams = {}
    for i in range(length_full_text):
        tup = (full_text_string[i], full_text_string[i+1])
        ngrams.setdefault(tup,[]).append(full_text_string[i+2])

    return ngrams,(full_text_string.pop(-2), full_text_string.pop(-1))


#green_eggs = make_chains("green-eggs.txt")
#print green_eggs
def make_text(dict1, dict2):
    """Takes dictionary of markov chains; returns random text."""
    
    dictionaries = [dict1, dict2]
    pick_dict = random.choice(dictionaries)
    start = random.choice(pick_dict.keys())
    first_word = start[-1]
    next = random.choice(pick_dict[start])
    result = list(start)
    result.append(next)
    #print " ".join(result)

    while next[-1] != ".":
        new = tuple([first_word, next])
        pick_dict_again = random.choice(dictionaries)

        if new in pick_dict_again:
            next = random.choice(pick_dict_again[new])
        else:
            for dictionary in dictionaries:
                if dictionary != pick_dict_again:
                    next = random.choice(dictionary[new])
        result.append(next)
        first_word = result[-2]
        next = result[-1]


    return " ".join(result)   

#make_text(green_eggs)

    # return "Here's some random text."


# Change this to read input_text from a file, deciding which file should
# be used by examining the `sys.argv` arguments (if neccessary, see the
# Python docs for sys.argv)
# print str(sys.argv)

functions = sys.argv[0]
text = sys.argv[1]
text2 = sys.argv[2]

# # Get a Markov chain
chain_dict = make_chains(text)[0]
chain_dict2 = make_chains(text2)[0]

# # Produce random text
random_text = make_text(chain_dict, chain_dict2)

print random_text
