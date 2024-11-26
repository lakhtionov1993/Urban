class WordsFinder:
    def __init__(self, *file_names):
        self.file_names = file_names

    def get_all_words(self):
        all_words = {}
        for file_name in self.file_names:
            with open(file_name, 'r', encoding='utf-8') as file:
                words = []
                for i in file:
                    i = i.lower()
                    punctuation = [',', '.', '=', '!', '?', ';', ':']
                    for punct in punctuation:
                        i = i.replace(punct, '')
                    i = i.replace(' - ', ' ')
                    words.extend(i.split())
                all_words[file_name] = words
        return all_words

    def find(self, word):
        places = {}
        for key, value in self.get_all_words().items():
            if word.lower() in value:
                places[key] = value.index(word.lower()) + 1
        return places

    def count(self, word):
        counters = {}
        for value, key in self.get_all_words().items():
            words_count = key.count(word.lower())
            counters[value] = words_count
        return counters


if __name__ == '__main__':
    finder1 = WordsFinder('Rudyard Kipling - If.txt', )
    print(finder1.get_all_words())
    print(finder1.find('if'))
    print(finder1.count('if'))

    finder2 = WordsFinder('test_file.txt')
    print(finder2.get_all_words())  # Все слова
    print(finder2.find('TEXT'))  # 3 слово по счёту
    print(finder2.count('teXT'))  # 4 слова teXT в тексте всего
