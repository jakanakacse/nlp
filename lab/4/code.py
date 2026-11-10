from nltk.stem import PorterStemmer, LancasterStemmer, SnowballStemmer

porter = PorterStemmer()
lancaster = LancasterStemmer()
snowball = SnowballStemmer('english')

words = ["connection", "connecting", "connections", "programming", "fairly", "generously", "studies", "universal"]

print(f"{'Word':<15} {'Porter':<15} {'Lancaster':<15} {'Snowball':<15}")
print("=" * 60)

for word in words:
    p = porter.stem(word)
    l = lancaster.stem(word)
    s = snowball.stem(word)
    print(f"{word:<15} {p:<15} {l:<15} {s:<15}")

