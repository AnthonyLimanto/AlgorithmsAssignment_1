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
        self.root = None

        for words in words_frequencies:
            self.add_word_frequency(words)


    def search(self, word: str) -> int:
        """
        search for a word
        @param word: the word to be searched
        @return: frequency > 0 if found and 0 if NOT found
        """
        result = 0
        result = self._search(self.root, word, 0)

        return result

    def add_word_frequency(self, word_frequency: WordFrequency) -> bool:
        """
        add a word and its frequency to the dictionary
        @param word_frequency: (word, frequency) to be added
        :return: True whether succeeded, False when word is already in the dictionary
        """

        #print("NEW WORD")
        result = 0
        result = self._search(self.root, word_frequency.word, 0)
        #print("ADD SEARCH RESULT: ", result, "FOR WORD: ", word_frequency.word)

        if result == 0:
            self.root = self.insert(self.root, word_frequency.word, word_frequency.frequency, 0)
            return True
        else:
            return False


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


    def insert(self, root, string, frequency, index):

        char = string[index]

        if root is None:
            root = Node(letter= char)

        if char < root.letter:
            root.left = self.insert(root.left, string, frequency, index)
        
        elif char > root.letter:
            root.right = self.insert(root.right, string, frequency, index)

        elif index < len(string) - 1:
            root.middle = self.insert(root.middle, string, frequency, index + 1)
        else:
            root.frequency = frequency
            root.end_word = True

        return root


    def _search(self, node : Node, string, index) -> int:

        char = string[index]

        #print("SEARCH AT NODE: ", char)
        
        if node == None:
            return 0

        if char < node.letter:
            #print("GOING LEFT")
            return self._search(node.left, string, index)
        
        elif char > node.letter:
            #print("GOING RIGHT")

            return self._search(node.right, string, index)

        elif index < len(string) - 1:
            #print("GOING MIDDLE")
            return self._search(node.middle, string, index + 1)
        else:
            #print("NODE FREQUENCY: ", node.frequency)
            if node.frequency != None:
                result = node.frequency
            else:
                result = 0
            #print("METHOD'S RESULT: ", result)
            return result