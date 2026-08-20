import string
from collections import Counter


class TextAnalyzer:

    def __init__(self, text):
        self.text = text

    def clean_text(self):
        # Convert to lowercase
        text = self.text.lower()

        # Remove punctuation
        text = text.translate(str.maketrans("", "", string.punctuation))

        # Remove extra whitespace
        text = " ".join(text.split())

        return text

    def get_words(self):
        cleaned = self.clean_text()
        return cleaned.split()

    def total_word_count(self):
        return len(self.get_words())

    def find_palindromes(self):
        words = self.get_words()

        # Use set to avoid duplicate palindrome words
        palindromes = {
            word for word in words
            if len(word) > 1 and word == word[::-1]
        }

        return sorted(palindromes)

    def frequency_table(self):
        words = self.get_words()
        return Counter(words)

    def report(self):
        print("----- TEXT ANALYSIS REPORT -----")
        print("Total Words:", self.total_word_count())

        print("\nPalindromes:")
        print(self.find_palindromes())

        print("\nWord Frequency:")
        for word, count in sorted(self.frequency_table().items()):
            print(f"{word}: {count}")


# Multiline string input
text = """
Madam went to the market.
She saw a level building and a civic center.
Madam returned home.
"""

analyzer = TextAnalyzer(text)
analyzer.report()