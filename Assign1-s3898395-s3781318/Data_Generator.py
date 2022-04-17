import sys
from dictionary.node import Node
from dictionary.word_frequency import WordFrequency
from dictionary.base_dictionary import BaseDictionary
from dictionary.list_dictionary import ListDictionary
from dictionary.hashtable_dictionary import HashTableDictionary
from dictionary.ternarysearchtree_dictionary import TernarySearchTreeDictionary
import random as rd

# program randomly makes data sets in increasing size, a little slow but its is manageable
# use by entering in the terminal
# python3 Data_Generator.py sampleData200k


if __name__ == '__main__':
    # Fetch the command line arguments
    args = sys.argv

    

    # read from data file to populate the initial set of points
    data_filename = args[1]
    words_frequencies_from_file = []
    try:
        data_file = open(data_filename, 'r')
        for line in data_file:
            values = line.split()
            word = values[0]
            frequency = int(values[1])
            word_frequency = WordFrequency(word, frequency)  # each line contains a word and its frequency
            words_frequencies_from_file.append(word_frequency)
        data_file.close()
    except FileNotFoundError as e:
        print("Data file doesn't exist.")
    


    # list of file names
    file_names = ['sample_500.txt', 'sample_1000.txt', 'sample_5000.txt', 'sample_10000.txt', 'sample_50000.txt', 'sample_100000.txt', 'sample_150000.txt']
    number_of_words = [500, 1000, 5000, 10000, 50000, 100000, 150000]


    # writes to each file
    num = 0
   
    for count in number_of_words:
        output_file = open(file_names[num], 'w')
        tmp = words_frequencies_from_file.copy()
        while count > 0:
            x = rd.randint(0, len(tmp)-1)
            
            output_file.write(f"{tmp[x].word} {tmp[x].frequency}\n")
            tmp.remove(tmp[x])
            count -= 1
           

        output_file.close()
        num = num + 1

    # writes to last file
    output_file = open('sample2_200000.txt', 'w')
    while len(words_frequencies_from_file) != 0:
        x = rd.randint(0, len(words_frequencies_from_file)-1)
        output_file.write(f"{words_frequencies_from_file[x].word} {words_frequencies_from_file[x].frequency}\n")
        words_frequencies_from_file.remove(words_frequencies_from_file[x])
    output_file.close
    