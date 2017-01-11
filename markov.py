from random import choice


def open_and_read_file(file_path):
    """Takes file path as string; returns text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """

    corpus = open(file_path).read()

    return corpus


def make_chains(input_text):
    """Takes input text as string; returns _dictionary_ of markov chains.

    A chain will be a key that consists of a tuple of (word1, word2)
    and the value would be a list of the word(s) that follow those two
    words in the input text.

    For example:

        >>> make_chains("hi there mary hi there juanita")
        {('hi', 'there'): ['mary', 'juanita'], ('there', 'mary'): ['hi'], ('mary', 'hi': ['there']}
    """

    words = open_and_read_file(input_text).split()
    chains = {}
    for i in range(len(words)-2):
        my_tuple = words[i], words[i + 1]
        new_value = words[i+2]

        if my_tuple not in chains:
            chains[(my_tuple)] = [new_value]
        else:
            chains[my_tuple].append(new_value)

    return chains


def make_text(chains):
    """Takes dictionary of markov chains; returns random text."""

    random_text = ""
    key = choice(chains.keys())
    print key
    words = key[0], key[1]
    random_text = random_text + key[0] + " " + key[1]
    
    # # if key in chains:
    next_word = choice(chains[key])
    print next_word
    #print "next word is " + next_word
    random_text = random_text + " " + next_word
    new_key = key[1], next_word
    
    print new_key, type(new_key)

    text = []

    while new_key in chains:
        #print new_key
        next_word = choice(chains[new_key])
        # print next_word

        text.append(next_word)

        # print text
        # random_text = random_text + " " + next_word
        # next_word = choice(chains[new_key])
        new_key = new_key[1], next_word

        print " ".join(text)
        # print random_text
    
    
   
    # print chains[key]
    # print key
    # print words
    # print "next word is " + next_word
    # print random_text
    # print new_key

    # return random_text    

    # print new_string
    

# input_path = "gettysburg.txt"

# # Open the file and turn it into one long string
# input_text = open_and_read_file(input_path)

# # Get a Markov chain
# chains = make_chains(input_text)

# # Produce random text
# random_text = make_text(chains)

# print random_text
