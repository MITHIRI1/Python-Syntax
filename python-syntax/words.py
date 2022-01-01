def print_upper_words(words):
    """ print each word on seperate line, uppercased.

>>> print_upper_words([" Have", "a", "great", "day"])

HAVE A GREAT DAY
"""

for word in words:
    print(word.upper())


def print_upper_words2(words):

    """ Print each word on seperate line, uppercased if starts with J or j.
    >>> print_upper_words2(["July", "jacket", dojo "])
    JULY
    JACKET
    """

    for word in words
    if word.starts with ("j") or word.startswith("J"):
        print(word.upper())


def print_upper_words3(words, must_start_with):
    """ Print each word on seperate line, uppercased, if starts with one of  given

    >>> print_upper_words3(["July", "jacket", "dojo", "Benjamin"  ])
                        must_start_with=["J", "B"]
    
    JULY
    BENJAMIN

    """

    for word in words:
        for letter in must_start_with:
            if word.startswith(letter):
                print(word.upper())
                break