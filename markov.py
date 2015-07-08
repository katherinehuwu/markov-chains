import sys
import random


def make_chains(corpus, n=2):
    """Takes input text as string; returns dictionary of markov chains."""
    text_file = open(corpus)
    full_text_string = []
    for line in text_file:
        text_list = line.rstrip().split()
        full_text_string.extend(text_list)
    
    #print full_text_string
    
    length_full_text = len(full_text_string)-n
    ngrams = {}
    for i in range(length_full_text):
        pre_tup = []
        for j in range(n):
            pre_tup.append(full_text_string[i+j])
        tup = tuple(pre_tup)
        ngrams.setdefault(tup,[]).append(full_text_string[i+n])

    return ngrams

#green_eggs = make_chains("green-eggs.txt")
#print green_eggs
def make_text(chains, n=2):
    """Takes dictionary of markov chains; returns random text."""
    start = random.choice(chains.keys())
    first_word = list(start[-(n-1):]) 
    next = random.choice(chains[start])
    result = list(start)
    result.append(next)


    while next[-1].isalpha():
        new = tuple(first_word+[next]) #should be list converted to tuple--make sure it create n tuple
        print new
        next_word = random.choice(chains[new]) #check to see if changing variable "next" works
        
        print "This is next_word: ", next_word
        result.append(next_word)
        first_word = result[-n:-(n-1)] #check index--work here!
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

input_text = text

# # Get a Markov chain
chain_dict = make_chains(input_text, 3)

# # Produce random text
random_text = make_text(chain_dict, 3)

print random_text
