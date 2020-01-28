class WChainProcessor:

    def find_length_of_word_chain(self, file_in):
        words = self.__get_wchain_from_file(file_in)
        if len(words) == 0:
            return 0
        if len(words) == 1:
            return 1
        memo = dict()

        def find_length_for_word(word):
            if len(word) == 0:
                return 0
            if word in memo:
                return memo[word]
            if len(word) == 1:
                memo[word] = 1
                return 1
            elif word not in memo:
                subwords = []
                for i in range(len(word)):
                    s = word[:i] + word[i + 1:]
                    if s in words:
                        subwords.append(s)
                if len(subwords) == 0:
                    memo[word] = 1
                elif len(subwords) == 1:
                    memo[word] = find_length_for_word(subwords[0]) + 1
                else:
                    memo[word] = max(*[find_length_for_word(w) for w in subwords]) + 1
                return memo[word]

        for word in words:
            find_length_for_word(word)
        return max(*memo.values())

    def __get_wchain_from_file(self, file_in):
        words = []
        with open(file_in) as file:
            dict_len = int(file.readline())
            for i in range(dict_len):
                words.append(file.readline())
        return words
