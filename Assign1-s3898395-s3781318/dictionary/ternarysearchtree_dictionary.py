
from pkg_resources import working_set
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

    def build_dictionary(self, words_frequencies: [WordFrequency]):
        """
        construct the data structure to store nodes
        @param words_frequencies: list of (word, frequency) to be stored
        """
        self.root = None
        # TO BE IMPLEMENTED
        for words in words_frequencies:
            self.add_word_frequency(words)



    def search(self, word: str) -> int:
        """
        search for a word
        @param word: the word to be searched
        @return: frequency > 0 if found and 0 if NOT found
        """
        # TO BE IMPLEMENTED
        node = self._search(self.root, word, 0)
        if node == None:
            return 0
        

        # place holder for return
        return node.frequency

    def add_word_frequency(self, word_frequency: WordFrequency) -> bool:
        """
        add a word and its frequency to the dictionary
        @param word_frequency: (word, frequency) to be added
        :return: True whether succeeded, False when word is already in the dictionary
        """
        # TO BE IMPLEMENTED
            
        if self.search(word_frequency.word) == 0:
            return False
            
        self.root = self.insert(self.root, word_frequency.word, word_frequency.frequency, 0)

        # use search to if is in dict already
        # place holder for return
        return True

    def delete_word(self, word: str) -> bool:
        """
        delete a word from the dictionary
        @param word: word to be deleted
        @return: whether succeeded, e.g. return False when point not found
        """
        # TO BE IMPLEMENTED
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


    # I put this here
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
    
    # i put this here
    def _search(self, node, string, index):

        if node == None:
            return None

        char = string[index]

        if char < node.letter:
            node.left = self._search(node.left, string, index)
        
        elif char > node.letter:
            node.right = self._search(node.right, string, index)

        elif index < len(string) - 1:
            node.middle = self._search(node.middle, string, index + 1)
        else:
            return node
