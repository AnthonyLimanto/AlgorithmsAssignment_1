from dictionary.word_frequency import WordFrequency
from dictionary.base_dictionary import BaseDictionary


# ------------------------------------------------------------------------
# This class is required TO BE IMPLEMENTED. List-based dictionary implementation.
#
# __author__ = 'Son Hoang Dau'
# __copyright__ = 'Copyright 2022, RMIT University'
# ------------------------------------------------------------------------

class ListDictionary(BaseDictionary):

    def build_dictionary(self, words_frequencies: [WordFrequency]):
        """
        construct the data structure to store nodes
        @param words_frequencies: list of (word, frequency) to be stored
        """

        self.list_dict = []
        for words in words_frequencies:
            tmp = WordFrequency(words.word, words.frequency)
            self.list_dict.append(tmp)

    def search(self, word: str) -> int:
        """
        search for a word
        @param word: the word to be searched
        @return: frequency > 0 if found and 0 if NOT found
        """
        freq = 0

        for i in range(len(self.list_dict)):
            if self.list_dict[i].word == word:
                freq = self.list_dict[i].frequency

        return freq

    def add_word_frequency(self, word_frequency: WordFrequency) -> bool:
        """
        add a word and its frequency to the dictionary
        @param word_frequency: (word, frequency) to be added
        :return: True whether succeeded, False when word is already in the dictionary
        """
        found = False

        for i in range(len(self.list_dict)):
            if self.list_dict[i].word == word_frequency.word:
                found = True

        if found == True:
            return False
        else:
            tmp = WordFrequency(word_frequency.word, word_frequency.frequency)
            self.list_dict.append(tmp)
            return True

    def delete_word(self, word: str) -> bool:
        """
        delete a word from the dictionary
        @param word: word to be deleted
        @return: whether succeeded, e.g. return False when point not found
        """
        found = False
        targIndex = None

        for i in range(len(self.list_dict)):
            if self.list_dict[i].word == word:
                found = True
                targIndex = i
        
        if found == True:
            self.list_dict.pop(targIndex)
            return True
        else:
            return False

    def autocomplete(self, prefix_word: str) -> [WordFrequency]:
        """
        return a list of 3 most-frequent words in the dictionary that have 'prefix_word' as a prefix
        @param prefix_word: word to be autocompleted
        @return: a list (could be empty) of (at most) 3 most-frequent words with prefix 'prefix_word'
        """
        auto_complete_list = []
        tmp_dict = self.list_dict.copy()

        for x in range(3):
            found = False
            highest_index = 0
            highest_freq = 0
            highest_word = ""
            for i in range(len(tmp_dict)):
                if tmp_dict[i].word.startswith(prefix_word):
                    if tmp_dict[i].frequency > highest_freq:
                        found = True
                        highest_index = i
                        highest_freq = tmp_dict[i].frequency
                        highest_word = tmp_dict[i].word
            if found == True:
                wf_list = WordFrequency(highest_word, highest_freq)
                auto_complete_list.append(wf_list)
                tmp_dict.pop(highest_index)

        return auto_complete_list
