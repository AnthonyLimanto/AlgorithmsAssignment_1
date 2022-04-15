from dictionary.base_dictionary import BaseDictionary
from dictionary.word_frequency import WordFrequency
from dictionary.node import Node


# ------------------------------------------------------------------------
# This class is required to be implemented. Ternary Search Tree implementation.
#
# __author__ = 'Son Hoang Dau'
# __copyright__ = 'Copyright 2022, RMIT University'
# ------------------------------------------------------------------------


class TernarySearchTreeDictionary(BaseDictionary):

    def __init__(self):
        self.root = None

    def build_dictionary(self, words_frequencies: [WordFrequency]):
        """
        construct the data structure to store nodes
        @param words_frequencies: list of (word, frequency) to be stored
        """
        # TO BE IMPLEMENTED
        self.root = None

        for words in words_frequencies:
            self.add_word_frequency(words)


    def search(self, word: str) -> int:
        """
        search for a word
        @param word: the word to be searched
        @return: frequency > 0 if found and 0 if NOT found
        """
        searchRes = self._search(self.root, word)
        # place holder for return
        return searchRes

    def add_word_frequency(self, word_frequency: WordFrequency) -> bool:
        """
        add a word and its frequency to the dictionary
        @param word_frequency: (word, frequency) to be added
        :return: True whether succeeded, False when word is already in the dictionary
        """
        # TO BE IMPLEMENTED
        print("NEW WORD")
        self.root = self.insert(self.root, word_frequency.word, word_frequency.frequency, False)
        # place holder for return
        return True

    def delete_word(self, word: str) -> bool:
        """
        delete a word from the dictionary
        @param word: word to be deleted
        @return: whether succeeded, e.g. return False when point not found
        """
        # TO BE IMPLEMENTED
        #self._search(self.root), word)
        # place holder for return
        return False

    def autocomplete(self, word: str) -> [str]:
        """
        return a list of 3 most-frequent words in the dictionary that have 'word' as a prefix
        @param word: word to be autocompleted
        @return: a list (could be empty) of (at most) 3 most-frequent words with prefix 'word'
        """
        # TO BE IMPLEMENTED
        # place holder for return
        return []

    def insert(self, node, word, frequency, end_word): # Might be overwriting end_word field
        if len(word) == 0:
            return node
        
        head = word[0]
        tail = word[1:]
        if len(word) == 1:
            end_word = True

        if node is None:
            node = Node(head, frequency, end_word)
            print(node.letter, node.frequency, node.end_word, node) 
        
        if head < node.letter:
            node.left = self.insert(node.left, word, frequency, end_word)
        elif head > node.letter:
            node.right = self.insert(node.left, word, frequency, end_word)
        else:
            if len(tail) == 0 :
                end_word = True
            else : 
                node.middle = self.insert(node.middle, tail, frequency, end_word)
        
        return node

    def _search(self, node : Node, word): # Finds freq but then does backwards funky stuff and returns none each time until it rebuilds the word :D
        print("START SEARCH")

        if node == None or len(word) == 0:
            return 0
        
        head = word[0]
        tail = word[1:]

        if head < node.letter:
            self._search(node.left, word)
        elif head > node.letter:
            self._search(node.right, word)
        else:
            if head == node.letter:
                if len(tail) == 0: #and node.end_word == True
                    retVal = node.frequency
                    print("SEARCH: ",retVal)
                    return retVal
                else:
                    print("MIDDLE")
                    self._search(node.middle, tail)