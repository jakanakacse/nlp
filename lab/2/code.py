from nltk.stem import PorterStemmer

def word_analysis(word):
    stemmer = PorterStemmer()
    stem = stemmer.stem(word)
    suffix = word[len(stem):] if word.startswith(stem) else ""
    return {"Word": word, "Stem": stem, "Suffix": suffix}

def word_generation(root):
    return {
        "Base": root,
        "Plural/3rd Person": root + "es" if root.endswith(('s', 'sh', 'ch', 'x', 'z')) else root + "s",
        "Past Tense": root + "d" if root.endswith('e') else root + "ed",
        "Continuous": root[:-1] + "ing" if root.endswith('e') else root + "ing"
    }

print("--- Word Analysis ---")
for k, v in word_analysis("playing").items():
    print(f"{k}: {v}")

print("\n--- Word Generation ---")
for k, v in word_generation("play").items():
    print(f"{k}: {v}")

