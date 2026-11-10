import nltk
from nltk.wsd import lesk
from nltk.tokenize import word_tokenize

nltk.download('punkt', quiet=True)
nltk.download('punkt_tab', quiet=True)
nltk.download('wordnet', quiet=True)
nltk.download('omw-1.4', quiet=True)

ambiguous_samples = [
    ("bank", "I deposited my money in the bank."),
    ("apple", "Apple released a new smartphone yesterday."),
    ("crane", "A large crane was lifting heavy steel on the construction site."),
    ("plant", "The manufacturing plant produces thousands of cars each day."),
    ("mouse", "Click the left button of the computer mouse.")
]

for word, sentence in ambiguous_samples:
    tokens = word_tokenize(sentence)
    synset = lesk(tokens, word)
    print(f"Word: {word}")
    print(f"Sentence: {sentence}")
    print(f"Sense: {synset.name() if synset else 'None'}")
    print(f"Definition: {synset.definition() if synset else 'None'}")
    print("-" * 50)

