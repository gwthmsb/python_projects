
import operator, collections

"""
    This scripts reads through given file and prints top five occurring words in a given file
"""

def _parsing_file_contents(file_name):
    words_dict = dict()
    if not file_name:
        print("Empty file. Please provide filename")
        exit(2)
    else:
        with open(file_name, "r") as file:
            for line in file:
                # Split the line by space and add it to dict
                words = line.split(" ")
                for word in words:
                    word = word.strip()
                    value = words_dict.get(word, 0)
                    words_dict[word] = value+1
    v = collections.OrderedDict(sorted(words_dict.items(), key=operator.itemgetter(1), reverse=True))
    return v


def main():
    """
        1) Read through file and add words to dict
        2) Iterate through dict and add words to ordered dict. Keep least value out of 5 for comparision
        3) Get top five values
    """
    file_name = "topFiveWords.txt"
    word_dict = _parsing_file_contents(file_name)
    print(word_dict)

    print("Top two elements are: ")
    for i, k in enumerate(word_dict):
        print(k, ": ", word_dict.get(k))
        if i == 1:
            break


if __name__ == "__main__":
    main()