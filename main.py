from wchain import WChainProcessor
import sys

if __name__ == '__main__':
    processor = WChainProcessor()
    print(processor.find_length_of_word_chain(sys.argv[1]))
