import nltk
from nltk.stem import WordNetLemmatizer
from nltk.util import ngrams
from nltk.tokenize import word_tokenize
from collections import Counter

nltk.download('punkt', quiet=True)
nltk.download('punkt_tab', quiet=True)
nltk.download('wordnet', quiet=True)
nltk.download('omw-1.4', quiet=True)

text = "natural language processing with python is fun and language processing is powerful"
tokens = word_tokenize(text.lower())

print("--- a) Morphological Analysis ---")
lemmatizer = WordNetLemmatizer()
sample_words = ["running", "cats", "better", "studied"]
for w in sample_words:
    print(f"Word: {w:<10} Lemma (v): {lemmatizer.lemmatize(w, pos='v'):<10} Lemma (n): {lemmatizer.lemmatize(w, pos='n')}")

print("\n--- b) N-Grams Generation ---")
bigrams = list(ngrams(tokens, 2))
trigrams = list(ngrams(tokens, 3))
print("Bigrams:", bigrams)
print("Trigrams:", trigrams)

print("\n--- c) N-Grams Smoothing (Laplace Add-1) ---")
unigram_counts = Counter(tokens)
bigram_counts = Counter(bigrams)
vocab_size = len(unigram_counts)

def laplace_smoothing(w1, w2):
    bigram = (w1, w2)
    count_w1_w2 = bigram_counts[bigram]
    count_w1 = unigram_counts[w1]
    prob = (count_w1_w2 + 1) / (count_w1 + vocab_size)
    return prob

pair = ("language", "processing")
unseen_pair = ("language", "python")

print(f"P({pair[1]} | {pair[0]}) with Laplace Smoothing = {laplace_smoothing(*pair):.4f}")
print(f"P({unseen_pair[1]} | {unseen_pair[0]}) with Laplace Smoothing = {laplace_smoothing(*unseen_pair):.4f}")

