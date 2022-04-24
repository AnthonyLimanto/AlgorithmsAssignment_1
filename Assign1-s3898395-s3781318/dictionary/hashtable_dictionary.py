from dictionary import word_frequency
from dictionary.base_dictionary import BaseDictionary
from dictionary.word_frequency import WordFrequency


# ------------------------------------------------------------------------
# This class is required TO BE IMPLEMENTED. Hash-table-based dictionary.
#
# __author__ = 'Son Hoang Dau'
# __copyright__ = 'Copyright 2022, RMIT University'
# ------------------------------------------------------------------------

class HashTableDictionary(BaseDictionary):

    def build_dictionary(self, words_frequencies: [WordFrequency]):
        """
        construct the data structure to store nodes
        @param words_frequencies: list of (word, frequency) to be stored
        """
        self.this_dict = {}
        for words in words_frequencies:
            self.this_dict[words.word] = words.frequency
        



    def search(self, word: str) -> int:
        """
        search for a word
        @param word: the word to be searched
        @return: frequency > 0 if found and 0 if NOT found
        """
        freq = 0
        if word in self.this_dict:
            freq = self.this_dict.get(word)
            return freq
        else:
            return 0
                

    def add_word_frequency(self, word_frequency: WordFrequency) -> bool:
        """
        add a word and its frequency to the dictionary
        @param word_frequency: (word, frequency) to be added
        :return: True whether succeeded, False when word is already in the dictionary
        """

        if word_frequency.word in self.this_dict:
            return False
        
        self.this_dict[word_frequency.word] = word_frequency.frequency
        
        return True

    def delete_word(self, word: str) -> bool:
        """
        delete a word from the dictionary
        @param word: word to be deleted
        @return: whether succeeded, e.g. return False when point not found
        """

        if word in self.this_dict:
            self.this_dict.pop(word)
            return True

        return False

    def autocomplete(self, prefix_word: str) -> [WordFrequency]:
        """
        return a list of 3 most-frequent words in the dictionary that have 'word' as a prefix
        @param word: word to be autocompleted
        @return: a list (could be empty) of (at most) 3 most-frequent words with prefix 'word'
        """

        auto_complete_words = []
        tmp_dict = self.this_dict.copy()
        for x in range(3):
            found = False
            highest_frequency = 0
            most_frequent = ""
            for word_in_dict in tmp_dict:
                if word_in_dict.startswith(prefix_word):
                    if tmp_dict.get(word_in_dict) > highest_frequency:
                        highest_frequency = tmp_dict.get(word_in_dict)
                        most_frequent = word_in_dict
                        found = True
            if (found == True):          
                del tmp_dict[most_frequent]
                word_frequency = WordFrequency(most_frequent, highest_frequency)
                auto_complete_words.append(word_frequency)
            
        return auto_complete_words