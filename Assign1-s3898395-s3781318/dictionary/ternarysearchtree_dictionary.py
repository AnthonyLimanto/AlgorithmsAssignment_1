from dictionary.base_dictionary import BaseDictionary
from dictionary.word_frequency import WordFrequency
from dictionary.node import Node

import time
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
        result = 0
        result = self._search(self.root, word_frequency.word, 0)

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

        if self.search(word) == 0:
            return False
        else:
            self.root = self._delete(self.root, word, 0)
            if self.search(word) == 0:
                return True
            else:
                return False

    def autocomplete(self, prefix_word: str) -> [WordFrequency]:
        """
        return a list of 3 most-frequent words in the dictionary that have 'word' as a prefix
        @param word: word to be autocompleted
        @return: a list (could be empty) of (at most) 3 most-frequent words with prefix 'word'
        """
        tmp_auto_complete_list = []
        auto_complete_list = []


        # Search for suffixes
        for word in self._autocomplete(self.root, prefix_word):
            wf = WordFrequency(prefix_word + word, self._search(self.root, prefix_word + word, 0))
            tmp_auto_complete_list.append(wf)

        # Check if whole word is there
        if self._search(self.root, prefix_word, 0) > 0:
            wf = WordFrequency(prefix_word, self._search(self.root, prefix_word, 0))
            tmp_auto_complete_list.append(wf)

        # Find th
        for x in range(3):
            found = False
            highest_index = 0
            highest_freq = 0
            highest_word = ""
            for i in range(len(tmp_auto_complete_list)):
                if tmp_auto_complete_list[i].frequency > highest_freq:
                    found = True
                    highest_index = i
                    highest_freq = tmp_auto_complete_list[i].frequency
                    highest_word = tmp_auto_complete_list[i].word
            if found == True:
                wf_list = WordFrequency(highest_word, highest_freq)
                auto_complete_list.append(wf_list)
                if tmp_auto_complete_list:
                    tmp_auto_complete_list.pop(highest_index)

        return auto_complete_list


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
        
        if node == None:
            return 0

        if char < node.letter:
            return self._search(node.left, string, index)
        
        elif char > node.letter:
            return self._search(node.right, string, index)

        elif index < len(string) - 1:
            return self._search(node.middle, string, index + 1)
        else:
            if node.frequency != None:
                result = node.frequency
            else:
                result = 0
            return result

    
    def _delete(self, node : Node, string, index):
        
        char = string[index]

        if node == None:
            return None


        children = self.countChildren(node)

        if char < node.letter:
            node.left =  self._delete(node.left, string, index)
        elif char > node.letter:
            node.right = self._delete(node.right, string, index)
        else:
            if index < len(string) - 1:
                node.middle = self._delete(node.middle, string, index + 1)
            elif node.end_word == True:
                node.frequency = None
                node.end_word = False
            else:
                return None

        if (children != self.countChildren(node) and children == 1 and node.end_word == False):
            return None

        return node

    
    def countChildren(self, node : Node) -> int:
        count = 0
        if (node.left != None):
            count += 1
        if (node.right != None):
            count += 1
        if (node.middle != None):
            count += 1

        return count


    def _autocomplete(self, node : Node, string):
        if node == None or len(string) == 0:
            return []
        head = string[0]
        tail = string[1:]

        if head < node.letter:
            return self._autocomplete(node.left, string)
        elif head > node.letter:
            return self._autocomplete(node.right, string)
        else:
            if len(tail) == 0:
                return self._suffixSearch(node.middle)
            return self._autocomplete(node.middle, tail)


    def _suffixSearch(self, node : Node):
        if node != None:
            if node.end_word == True:
                yield node.letter
        
        if node.left:
            for word in self._suffixSearch(node.left):
                yield word
        if node.right:
            for word in self._suffixSearch(node.right):
                yield word
        if node.middle:
            for word in self._suffixSearch(node.middle):
                yield node.letter + word
