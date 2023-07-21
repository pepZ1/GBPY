import re
from collections import Counter


def most_common_words(text, top_n=10):
    cleaned_text = re.sub(r'[^\w\s]', '', text).lower()

    words = cleaned_text.split()

    word_count = Counter(words)

    sorted_word_count = dict(sorted(word_count.items(), key=lambda item: item[1], reverse=True))

    most_common_words = list(sorted_word_count.keys())[:top_n]

    return most_common_words



text = "всем привет я ем омлет уже сто лет вот это да ведь это не беда, а я а он ведь это звон"
result = most_common_words(text)
print("10 самых частых слов:")
print(result)