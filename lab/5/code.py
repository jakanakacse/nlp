import nltk
from nltk import pos_tag
from nltk.tokenize import word_tokenize

nltk.download('punkt', quiet=True)
nltk.download('punkt_tab', quiet=True)
nltk.download('averaged_perceptron_tagger', quiet=True)
nltk.download('averaged_perceptron_tagger_eng', quiet=True)

words = ["apple", "quickly", "building", "jumped", "beautiful", "education", "under", "they", "read", "smart"]

tagged_words = pos_tag(words)
pos_dict = dict(tagged_words)

print("--- 10 Words POS Tagging ---")
for word, tag in tagged_words:
    print(f"{word:<15} -> {tag}")

def find_pos(word):
    result = pos_tag([word])
    return result[0][1]

query_word = "education"
print("\n--- Search POS for Given Word ---")
print(f"Word: '{query_word}' -> POS Tag: {find_pos(query_word)}")

