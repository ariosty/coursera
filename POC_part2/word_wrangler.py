"""
Student code for Word Wrangler game
"""

import urllib2
import codeskulptor
import poc_wrangler_provided as provided

WORDFILE = "http://codeskulptor-assets.commondatastorage.googleapis.com/assets_scrabble_words3.txt"


# Functions to manipulate ordered word lists

def remove_duplicates(list1):
    """
    Eliminate duplicates in a sorted list.

    Returns a new sorted list with the same elements in list1, but
    with no duplicates.

    This function can be iterative.
    """
    result = []
    length = len(list1)
    current = 0
    while (current < length):
        result.append(list1[current])
        end = current + 1
        while (end < length and
               list1[end] == list1[current]):
            end += 1
        current = end
    return result

def intersect(list1, list2):
    """
    Compute the intersection of two sorted lists.

    Returns a new sorted list containing only elements that are in
    both list1 and list2.

    This function can be iterative.
    """
    result = []
    red_list1 = remove_duplicates(list1)
    red_list2 = remove_duplicates(list2)
    length1 = len(red_list1)
    length2 = len(red_list2)
    idx1 = 0
    idx2 = 0
    while (idx1 < length1 and idx2 < length2):
        if (red_list1[idx1] < red_list2[idx2]):
            idx1 += 1
        elif (red_list1[idx1] > red_list2[idx2]):
            idx2 += 1
        else:
            result.append(red_list1[idx1])
            idx1 += 1
            idx2 += 1
    return result

# Functions to perform merge sort

def merge(list1, list2):
    """
    Merge two sorted lists.

    Returns a new sorted list containing all of the elements that
    are in either list1 and list2.

    This function can be iterative.
    """   
    result = []
    length1 = len(list1)
    length2 = len(list2)
    idx1 = 0
    idx2 = 0
    while (idx1 < length1 and idx2 < length2):
        if (list1[idx1] <= list2[idx2]):
            result.append(list1[idx1])
            idx1 += 1
        else:
            result.append(list2[idx2])
            idx2 += 1
    while (idx1 < length1):
        result.append(list1[idx1])
        idx1 += 1
    while (idx2 < length2):
        result.append(list2[idx2])
        idx2 += 1
    return result
                
def merge_sort(list1):
    """
    Sort the elements of list1.

    Return a new sorted list with the same elements as list1.

    This function should be recursive.
    """
    length = len(list1)
    if (length < 2):
        return list1
    left = merge_sort(list1[: length / 2])
    right = merge_sort(list1[length / 2 :])
    return merge(left, right)

# Function to generate all strings for the word wrangler game

def gen_all_strings(word):
    """
    Generate all strings that can be composed from the letters in word
    in any order.

    Returns a list of all strings that can be formed from the letters
    in word.

    This function should be recursive.
    """
    if ("" == word):
        return [""]
    first = word[0]
    rest = word[1:]
    rest_strings = gen_all_strings(rest)
    result = list(rest_strings)
    for string in rest_strings:
        length = len(string)
        for idx in range(length + 1):
            result.append(string[:idx] + first + string[idx:])
    return result

# Function to load words from a file

def load_words(filename):
    """
    Load word list from the file named filename.

    Returns a list of strings.
    """
    words_file = urllib2.urlopen(filename)
    result = []
    for line in words_file.readlines():
        result.append(line[:-1])
    return result

def run():
    """
    Run game.
    """
    words = load_words(WORDFILE)
    wrangler = provided.WordWrangler(words, remove_duplicates, 
                                     intersect, merge_sort, 
                                     gen_all_strings)
    provided.run_game(wrangler)

# Uncomment when you are ready to try the game
# run()
