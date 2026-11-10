import nltk
from nltk.corpus import cmudict

nltk.download('cmudict', quiet=True)

try:
    cmu = cmudict.dict()
except Exception:
    cmu = {}

# Fallback phonetic dictionary for offline/lab exam reproducibility
fallback_g2p = {
    "apple": ["AE1", "P", "AH0", "L"],
    "cat": ["K", "AE1", "T"],
    "nlp": ["EH1", "N", "EH1", "L", "P", "IY1"],
    "speech": ["S", "P", "IY1", "CH"],
    "python": ["P", "AY1", "TH", "AA2", "N"]
}

def g2p(word):
    w = word.lower()
    if w in cmu:
        return cmu[w][0]
    return fallback_g2p.get(w, ["Phonemes", "not", "found"])

sample_words = ["apple", "cat", "nlp", "speech", "python"]

print(f"{'Grapheme (Word)':<20} {'Phonemes (ARPAbet)'}")
print("=" * 50)
for word in sample_words:
    phonemes = g2p(word)
    print(f"{word:<20} {' '.join(phonemes)}")

