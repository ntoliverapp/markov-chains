"""Generate Markov text from text files."""

from random import choice


def open_and_read_file(file_path):
    """Take file path as string; return text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """

    green = open('green-eggs.txt', mode ='rt')
    return green.read()


def make_chains(text_string):
    """Take input text as string; return dictionary of Markov chains.

    A chain will be a key that consists of a tuple of (word1, word2)
    and the value would be a list of the word(s) that follow those two
    words in the input text.

    For example:

        >>> chains = make_chains('hi there mary hi there juanita')

    Each bigram (except the last) will be a key in chains:

        >>> sorted(chains.keys())
        [('hi', 'there'), ('mary', 'hi'), ('there', 'mary')]

    Each item in chains is a list of all possible following words:

        >>> chains[('hi', 'there')]
        ['mary', 'juanita']

        >>> chains[('there','juanita')]
        [None]
    """

    green_eggs = text_string.split()
    
    chains = {}

    for word in range(len(green_eggs)-1):
        bigram = (green_eggs[word], green_eggs[word + 1])
        if word == len(green_eggs)-2:
            if bigram in chains:
                chains[bigram].append(None)
            else:
                chains[bigram] = [None]
        
        elif bigram in chains:
            chains[bigram].append(green_eggs[word + 2])
        else:
            chains[bigram] = [green_eggs[word + 2]]
    print(chains)
    return chains


def make_text(chains):
    """Return text from chains."""
    bigram = chains
    
    key = choice(list(chains.keys()))
    words = [key[0], key[1]]
    word = choice(chains[key])

    while word is not None:
        key = (key[1], word)
        words.append(word)
        word = choice(chains[key])
        
    return ' '.join(words)

input_path = 'green-eggs.txt'

# Open the file and turn it into one long string
input_text = open_and_read_file(input_path)

# Get a Markov chain
chains = make_chains(input_text)

# Produce random text
random_text = make_text(chains)

print(random_text)
