import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

nltk.download('punkt', quiet=True)
nltk.download('punkt_tab', quiet=True)
nltk.download('stopwords', quiet=True)

text = "JKKNIU stands as a dedicated center for higher education, honoring the profound cultural and literary legacy of Bangladesh's national poet."

tokens = word_tokenize(text)
stop_words = set(stopwords.words('english'))

filtered_tokens = [w for w in tokens if w.lower() not in stop_words]

print("Tokens:", tokens)
print("Filtered Tokens:", filtered_tokens)

